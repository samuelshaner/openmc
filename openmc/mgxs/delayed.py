from __future__ import division

from collections import Iterable, OrderedDict
from numbers import Integral
import os
import sys
import copy
import abc

import numpy as np

import openmc
import openmc.checkvalue as cv
from openmc.mgxs import EnergyGroups
from openmc.mgxs import MGXS

if sys.version_info[0] >= 3:
    basestring = str


# Supported cross section types
DELAYED_MGXS_TYPES = ['delayed-nu-fission',
                      'chi-delayed',
                      'chi-prompt',
                      'beta']

# Maximum number of delayed groups
# TODO: Get value from OpenMC
MAX_DELAYED_GROUPS = 8

# Supported domain types
# TODO: Implement Mesh domains
DOMAIN_TYPES = ['cell',
                'distribcell',
                'universe',
                'material']

# Supported domain classes
# TODO: Implement Mesh domains
_DOMAINS = [openmc.Cell,
           openmc.Universe,
           openmc.Material]


class DelayedMGXS(MGXS):
    """A multi-group cross section for some energy group structure and delayed
    group structure within some spatial domain.

    This class can be used for both OpenMC input generation and tally data
    post-processing to compute spatially-homogenized and energy-integrated
    multi-group cross sections for deterministic neutronics calculations.

    """

    # This is an abstract class which cannot be instantiated
    __metaclass__ = abc.ABCMeta

    def __init__(self, domain=None, domain_type=None, energy_groups=None,
                 by_nuclide=False, name=''):
        super(DelayedMGXS, self).__init__(domain, domain_type,
                                          energy_groups, by_nuclide, name)

    @staticmethod
    def get_mgxs(mgxs_type, domain=None, domain_type=None,
                 energy_groups=None, by_nuclide=False, name=''):
        """Return a MGXS subclass object for some energy group structure within
        some spatial domain for some reaction type.

        This is a factory method which can be used to quickly create MGXS
        subclass objects for various reaction types.

        Parameters
        ----------
        mgxs_type : {'delayed-nu-fission', 'chi-delayed', 'beta'}
            The type of delayed multi-group cross section object to return
        domain : Material or Cell or Universe
            The domain for spatial homogenization
        domain_type : {'material', 'cell', 'distribcell', 'universe'}
            The domain type for spatial homogenization
        energy_groups : EnergyGroups
            The energy group structure for energy condensation
        by_nuclide : bool
            If true, computes cross sections for each nuclide in domain.
            Defaults to False
        name : str, optional
            Name of the multi-group cross section. Used as a label to identify
            tallies in OpenMC 'tallies.xml' file. Defaults to the empty string.

        Returns
        -------
        MGXS
            A subclass of the abstract MGXS class for the multi-group cross
            section type requested by the user

        """

        cv.check_value('mgxs_type', mgxs_type, MGXS_TYPES)

        if mgxs_type == 'delayed-nu-fission':
            mgxs = DelayedNuFission(domain, domain_type, energy_groups)
        elif mgxs_type == 'chi-delayed':
            mgxs = ChiDelayed(domain, domain_type, energy_groups)
        elif mgxs_type == 'chi-prompt':
            mgxs = ChiPrompt(domain, domain_type, energy_groups)
        elif mgxs_type == 'beta':
            mgxs = Beta(domain, domain_type, energy_groups)

        mgxs.by_nuclide = by_nuclide
        mgxs.name = name
        return mgxs

    def get_xs(self, groups='all', subdomains='all', nuclides='all',
               xs_type='macro', order_groups='increasing', value='mean',
               delayed_groups='all'):
        """Returns an array of multi-group cross sections.

        This method constructs a 2D NumPy array for the requested multi-group
        cross section data data for one or more energy groups and subdomains.

        Parameters
        ----------
        groups : Iterable of Integral or 'all'
            Energy groups of interest. Defaults to 'all'.
        delayed_groups : Iterable of Integral or 'all'
            Delayed neutron precursor groups of interest. Defaults to 'all'.
        subdomains : Iterable of Integral or 'all'
            Subdomain IDs of interest. Defaults to 'all'.
        nuclides : Iterable of str or 'all' or 'sum'
            A list of nuclide name strings (e.g., ['U-235', 'U-238']). The
            special string 'all' will return the cross sections for all nuclides
            in the spatial domain. The special string 'sum' will return the
            cross section summed over all nuclides. Defaults to 'all'.
        xs_type: {'macro', 'micro'}
            Return the macro or micro cross section in units of cm^-1 or barns.
            Defaults to 'macro'.
        order_groups: {'increasing', 'decreasing'}
            Return the cross section indexed according to increasing or
            decreasing energy groups (decreasing or increasing energies).
            Defaults to 'increasing'.
        value : str
            A string for the type of value to return - 'mean', 'std_dev' or
            'rel_err' are accepted. Defaults to 'mean'.

        Returns
        -------
        ndarray
            A NumPy array of the multi-group cross section indexed in the order
            each group, subdomain and nuclide is listed in the parameters.

        Raises
        ------
        ValueError
            When this method is called before the multi-group cross section is
            computed from tally data.

        """

        if self.xs_tally is None:
            msg = 'Unable to get cross section since it has not been computed'
            raise ValueError(msg)

        cv.check_value('value', value, ['mean', 'std_dev', 'rel_err'])
        cv.check_value('xs_type', xs_type, ['macro', 'micro'])

        filters = []
        filter_bins = []

        # Construct a collection of the domain filter bins
        if subdomains != 'all':
            cv.check_iterable_type('subdomains', subdomains, Integral)
            for subdomain in subdomains:
                filters.append(self.domain_type)
                filter_bins.append((subdomain,))

        # Construct list of energy group bounds tuples for all requested groups
        if groups != 'all':
            cv.check_iterable_type('groups', groups, Integral)
            for group in groups:
                filters.append('energy')
                filter_bins.append((self.energy_groups.get_group_bounds(group),))

        # Construct list of delayed groups
        if delayed_groups not in ['all', 'sum']:
            cv.check_iterable_type('delayed groups', delayed_groups, Integral)
            for group in delayed_groups:
                filters.append('delayedgroup')
                filter_bins.append((group,))
                
        # Construct a collection of the nuclides to retrieve from the xs tally
        if self.by_nuclide:
            if nuclides == 'all' or nuclides == 'sum' or nuclides == ['sum']:
                query_nuclides = self.get_all_nuclides()
            else:
                query_nuclides = nuclides
        else:
            query_nuclides = ['total']

        if delayed_groups == 'sum' or delayed_groups == ['sum']:
            xs_tally = self.xs_tally.summation(filter_type='delayedgroup',
                                               filters=range(1,MAX_DELAYED_GROUPS))
            
        # If user requested the sum for all nuclides, use tally summation
        if nuclides == 'sum' or nuclides == ['sum']:
            xs_tally = self.xs_tally.summation(nuclides=query_nuclides)
            xs = xs_tally.get_values(filters=filters, filter_bins=filter_bins,
                                     value=value)
        else:
            xs = self.xs_tally.get_values(filters=filters, filter_bins=filter_bins,
                                          nuclides=query_nuclides, value=value)
            
        # Divide by atom number densities for microscopic cross sections
        if xs_type == 'micro':
            if self.by_nuclide:
                densities = self.get_nuclide_densities(nuclides)
            else:
                densities = self.get_nuclide_densities('sum')
            if value == 'mean' or value == 'std_dev':
                xs /= densities[np.newaxis, :, np.newaxis]

        # Reverse data if user requested increasing energy groups since
        # tally data is stored in order of increasing energies
        if order_groups == 'increasing':
            if groups == 'all':
                num_groups = self.num_groups
            else:
                num_groups = len(groups)

            # Reshape tally data array with separate axes for domain and energy
            num_subdomains = xs.shape[0] / num_groups
            new_shape = (num_subdomains, num_groups) + xs.shape[1:]
            xs = np.reshape(xs, new_shape)

            # Reverse energies to align with increasing energy groups
            xs = xs[:, ::-1, :]

            # Eliminate trivial dimensions
            xs = np.squeeze(xs)
            xs = np.atleast_1d(xs)

        return xs

    def print_xs(self, subdomains='all', nuclides='all', xs_type='macro'):
        """Print a string representation for the multi-group cross section.

        Parameters
        ----------
        subdomains : Iterable of Integral or 'all'
            The subdomain IDs of the cross sections to include in the report.
            Defaults to 'all'.
        nuclides : Iterable of str or 'all' or 'sum'
            The nuclides of the cross-sections to include in the report. This
            may be a list of nuclide name strings (e.g., ['U-235', 'U-238']).
            The special string 'all' will report the cross sections for all
            nuclides in the spatial domain. The special string 'sum' will report
            the cross sections summed over all nuclides. Defaults to 'all'.
        xs_type: {'macro', 'micro'}
            Return the macro or micro cross section in units of cm^-1 or barns.
            Defaults to 'macro'.

        """

        # Construct a collection of the subdomains to report
        if subdomains != 'all':
            cv.check_iterable_type('subdomains', subdomains, Integral)
        elif self.domain_type == 'distribcell':
            subdomains = np.arange(self.num_subdomains, dtype=np.int)
        else:
            subdomains = [self.domain.id]

        # Construct a collection of the nuclides to report
        if self.by_nuclide:
            if nuclides == 'all':
                nuclides = self.get_all_nuclides()
            elif nuclides == 'sum':
                nuclides = ['sum']
            else:
                cv.check_iterable_type('nuclides', nuclides, basestring)
        else:
            nuclides = ['sum']

        cv.check_value('xs_type', xs_type, ['macro', 'micro'])

        # Build header for string with type and domain info
        string = 'Multi-Group XS\n'
        string += '{0: <16}=\t{1}\n'.format('\tReaction Type', self.rxn_type)
        string += '{0: <16}=\t{1}\n'.format('\tDomain Type', self.domain_type)
        string += '{0: <16}=\t{1}\n'.format('\tDomain ID', self.domain.id)

        # If cross section data has not been computed, only print string header
        if self.xs_tally is None:
            print(string)
            return

        # Loop over all subdomains
        for subdomain in subdomains:

            if self.domain_type == 'distribcell':
                string += '{0: <16}=\t{1}\n'.format('\tSubdomain', subdomain)

            # Loop over all Nuclides
            for nuclide in nuclides:

                # Build header for nuclide type
                if nuclide != 'sum':
                    string += '{0: <16}=\t{1}\n'.format('\tNuclide', nuclide)

                # Build header for cross section type
                if xs_type == 'macro':
                    string += '{0: <16}\n'.format('\tCross Sections [cm^-1]:')
                else:
                    string += '{0: <16}\n'.format('\tCross Sections [barns]:')

                # Loop over the delayed groups
                for delayed_group in range(1, MAX_DELAYED_GROUPS+1):

                    string += '{0: <16}{1: <2}\n'.format('\tDelayed Group:',
                                                         delayed_group)
                    template = '{0: <12}Group {1} [{2: <10} - {3: <10}MeV]:\t'
                  
                    # Loop over energy groups ranges
                    for group in range(1, self.num_groups+1):
                        bounds = self.energy_groups.get_group_bounds(group)
                        string += template.format('', group, bounds[0], bounds[1])
                        average = self.get_xs([group], [subdomain], [nuclide],
                                              xs_type=xs_type, value='mean',
                                              delayed_groups=[delayed_group])
                        rel_err = self.get_xs([group], [subdomain], [nuclide],
                                              xs_type=xs_type, value='rel_err',
                                              delayed_groups=[delayed_group])
                        average = average.flatten()[0]
                        rel_err = rel_err.flatten()[0] * 100.
                        string += '{:.2e} +/- {:1.2e}%'.format(average, rel_err)
                        string += '\n'
                    string += '\n'
                string += '\n'
            string += '\n'

        print(string)


class DelayedNuFissionXS(DelayedMGXS):
    """A fission delayed-neutron production multi-group cross section."""

    def __init__(self, domain=None, domain_type=None,
                 groups=None, by_nuclide=False, name=''):
        super(DelayedNuFissionXS, self).__init__(domain, domain_type,
                                                 groups, by_nuclide, name)
        self._rxn_type = 'delayed-nu-fission'

    def create_tallies(self):
        """Construct the OpenMC tallies needed to compute this cross section.

        This method constructs two tracklength tallies to compute the 'flux'
        and 'delayed-nu-fission' reaction rates in the spatial domain and energy
        groups of interest.

        """

        # Create a list of scores for each Tally to be created
        scores = ['flux', 'delayed-nu-fission']
        estimator = 'tracklength'
        keys = scores

        # Create the non-domain specific Filters for the Tallies
        group_edges = self.energy_groups.group_edges
        energy = openmc.Filter('energy', group_edges)
        delayedgroup = openmc.Filter('delayedgroup',
                                     range(1,MAX_DELAYED_GROUPS+1))
        filters = [[energy], [energy, delayedgroup]]

        # Initialize the Tallies
        super(DelayedNuFissionXS, self).create_tallies(scores, filters,
                                                       keys, estimator)

    def compute_xs(self):
        """Computes the multi-group nu-fission cross sections using OpenMC
        tally arithmetic."""

        self._xs_tally = self.tallies['delayed-nu-fission'] \
                         / self.tallies['flux']
        super(DelayedNuFissionXS, self).compute_xs()

class PromptNuFissionXS(MGXS):
    """A fission prompt-neutron production multi-group cross section."""

    def __init__(self, domain=None, domain_type=None,
                 groups=None, by_nuclide=False, name=''):
        super(PromptNuFissionXS, self).__init__(domain, domain_type,
                                                 groups, by_nuclide, name)
        self._rxn_type = 'prompt-nu-fission'

    def create_tallies(self):
        """Construct the OpenMC tallies needed to compute this cross section.

        This method constructs two tracklength tallies to compute the 'flux'
        and 'delayed-nu-fission' reaction rates in the spatial domain and energy
        groups of interest.

        """

        # Create a list of scores for each Tally to be created
        scores = ['flux', 'delayed-nu-fission', 'nu-fission']
        estimator = 'tracklength'
        keys = scores

        # Create the non-domain specific Filters for the Tallies
        group_edges = self.energy_groups.group_edges
        energy = openmc.Filter('energy', group_edges)
        filters = [[energy], [energy], [energy]]

        # Initialize the Tallies
        super(PromptNuFissionXS, self).create_tallies(scores, filters,
                                                       keys, estimator)

    def compute_xs(self):
        """Computes the multi-group nu-fission cross sections using OpenMC
        tally arithmetic."""

        self._xs_tally = (self.tallies['nu-fission'] - \
                          self.tallies['delayed-nu-fission']) \
                         / self.tallies['flux']
        super(PromptNuFissionXS, self).compute_xs()

class Beta(DelayedMGXS):
    """The delayed-neutron fraction in each group."""

    def __init__(self, domain=None, domain_type=None,
                 groups=None, by_nuclide=False, name=''):
        super(Beta, self).__init__(domain, domain_type,
                                   groups, by_nuclide, name)
        self._rxn_type = 'beta'

    def create_tallies(self):
        """Construct the OpenMC tallies needed to compute this cross section.

        This method constructs two tracklength tallies to compute the
        'delayed-nu-fission' and 'nu-fission' reaction rates in the spatial
        domain and energy groups of interest.

        """

        # Create a list of scores for each Tally to be created
        scores = ['delayed-nu-fission', 'nu-fission']
        estimator = 'tracklength'
        keys = scores

        # Create the non-domain specific Filters for the Tallies
        group_edges = self.energy_groups.group_edges
        energy = openmc.Filter('energy', group_edges)
        delayedgroup = openmc.Filter('delayedgroup',
                                     range(1,MAX_DELAYED_GROUPS+1))
        filters = [[energy, delayedgroup], [energy]]

        # Initialize the Tallies
        super(Beta, self).create_tallies(scores, filters, keys, estimator)

    def compute_xs(self):
        """Computes the multi-group nu-fission cross sections using OpenMC
        tally arithmetic."""

        self._xs_tally = self.tallies['delayed-nu-fission'] \
                         / self.tallies['nu-fission']
        super(Beta, self).compute_xs()


class ChiDelayed(DelayedMGXS):
    """The delayed-neutron fission spectrum."""

    def __init__(self, domain=None, domain_type=None,
                 groups=None, by_nuclide=False, name=''):
        super(ChiDelayed, self).__init__(domain, domain_type, groups,
                                         by_nuclide, name)
        self._rxn_type = 'chi-delayed'

    def create_tallies(self):
        """Construct the OpenMC tallies needed to compute this cross section.

        This method constructs two analog tallies to compute 'delayed-nu-fission'
        reaction rates with 'energy' and 'energyout' filters in the spatial
        domain and energy groups of interest.

        """

        # Create a list of scores for each Tally to be created
        scores = ['delayed-nu-fission', 'delayed-nu-fission']
        estimator = 'analog'
        keys = ['delayed-nu-fission-in', 'delayed-nu-fission-out']

        # Create the non-domain specific Filters for the Tallies
        group_edges = self.energy_groups.group_edges
        energyout = openmc.Filter('energyout', group_edges)
        energyin = openmc.Filter('energy', [group_edges[0], group_edges[-1]])
        delayedgroup = openmc.Filter('delayedgroup',
                                     range(1,MAX_DELAYED_GROUPS+1))
        filters = [[energyin], [energyout]]

        # Intialize the Tallies
        super(ChiDelayed, self).create_tallies(scores, filters, keys, estimator)

    def compute_xs(self):
        """Computes delayed chi fission spectrum using OpenMC tally arithmetic."""

        # Retrieve the fission production tallies
        delayed_nu_fission_in = self.tallies['delayed-nu-fission-in']
        delayed_nu_fission_out = self.tallies['delayed-nu-fission-out']

        # Remove coarse energy filter to keep it out of tally arithmetic
        energy_filter = delayed_nu_fission_in.find_filter('energy')
        delayed_nu_fission_in.remove_filter(energy_filter)

        # Compute delayed chi
        self._xs_tally = delayed_nu_fission_out / delayed_nu_fission_in

        # Add the coarse energy filter back to the nu-fission tally
        delayed_nu_fission_in.add_filter(energy_filter)

        super(ChiDelayed, self).compute_xs()

    def get_xs(self, groups='all', subdomains='all', nuclides='all',
               xs_type='macro', order_groups='increasing', value='mean',
               delayed_groups='all'):
        """Returns an array of the delayed-neutron fission spectrum.

        This method constructs a 2D NumPy array for the requested multi-group
        cross section data data for one or more energy groups and subdomains.

        Parameters
        ----------
        groups : Iterable of Integral or 'all'
            Energy groups of interest. Defaults to 'all'.
        delayed_groups: Iterable of Integral or 'all' or 'sum'
            Delayed neutron precursor groups
        subdomains : Iterable of Integral or 'all'
            Subdomain IDs of interest. Defaults to 'all'.
        nuclides : Iterable of str or 'all' or 'sum'
            A list of nuclide name strings (e.g., ['U-235', 'U-238']). The
            special string 'all' will return the cross sections for all nuclides
            in the spatial domain. The special string 'sum' will return the
            cross section summed over all nuclides. Defaults to 'all'.
        xs_type: {'macro', 'micro'}
            This parameter is not relevant for chi but is included here to
            mirror the parent MGXS.get_xs(...) class method
        order_groups: {'increasing', 'decreasing'}
            Return the cross section indexed according to increasing or
            decreasing energy groups (decreasing or increasing energies).
            Defaults to 'increasing'.
        value : str
            A string for the type of value to return - 'mean', 'std_dev', or
            'rel_err' are accepted. Defaults to 'mean'.

        Returns
        -------
        ndarray
            A NumPy array of the multi-group cross section indexed in the order
            each group, subdomain and nuclide is listed in the parameters.

        Raises
        ------
        ValueError
            When this method is called before the multi-group cross section is
            computed from tally data.

        """

        if self.xs_tally is None:
            msg = 'Unable to get cross section since it has not been computed'
            raise ValueError(msg)

        cv.check_value('value', value, ['mean', 'std_dev', 'rel_err'])
        cv.check_value('xs_type', xs_type, ['macro', 'micro'])

        filters = []
        filter_bins = []

        # Construct a collection of the domain filter bins
        if subdomains != 'all':
            cv.check_iterable_type('subdomains', subdomains, Integral)
            for subdomain in subdomains:
                filters.append(self.domain_type)
                filter_bins.append((subdomain,))

        # Construct list of energy group bounds tuples for all requested groups
        if groups != 'all':
            cv.check_iterable_type('groups', groups, Integral)
            for group in groups:
                filters.append('energyout')
                filter_bins.append((self.energy_groups.get_group_bounds(group),))

        # Construct list of delayed groups
        if delayed_groups not in ['all', 'sum']:
            cv.check_iterable_type('delayed groups', delayed_groups, Integral)
            for group in delayed_groups:
                filters.append('delayedgroup')
                filter_bins.append((group,))

        delayed_nu_fission_in = self.tallies['delayed-nu-fission-in']
        delayed_nu_fission_out = self.tallies['delayed-nu-fission-out']

        if delayed_groups == 'sum' or delayed_groups == ['sum']:
            delayed_nu_fission_in = delayed_nu_fission_in.summation(
                filter_type='delayedgroup', filters=range(1,MAX_DELAYED_GROUPS))
            delayed_nu_fission_out = delayed_nu_fission_out.summation(
                filter_type='delayedgroup', filters=range(1,MAX_DELAYED_GROUPS))

        # If chi was computed for each nuclide in the domain
        if self.by_nuclide:

            # Get the sum as the fission source weighted average chi for all
            # nuclides in the domain
            if nuclides == 'sum' or nuclides == ['sum']:
                
                # Retrieve the fission production tallies
                delayed_nu_fission_in = self.tallies['delayed-nu-fission-in']
                delayed_nu_fission_out = self.tallies['delayed-nu-fission-out']

                # Sum out all nuclides
                nuclides = self.get_all_nuclides()
                delayed_nu_fission_in = delayed_nu_fission_in.summation(nuclides=nuclides)
                delayed_nu_fission_out = delayed_nu_fission_out.summation(nuclides=nuclides)

                # Remove coarse energy filter to keep it out of tally arithmetic
                energy_filter = delayed_nu_fission_in.find_filter('energy')
                delayed_nu_fission_in.remove_filter(energy_filter)

                # Compute chi and store it as the xs_tally attribute so we can
                # use the generic get_xs(...) method
                xs_tally = delayed_nu_fission_out / delayed_nu_fission_in

                # Add the coarse energy filter back to the nu-fission tally
                delayed_nu_fission_in.add_filter(energy_filter)

                xs = xs_tally.get_values(filters=filters,
                                         filter_bins=filter_bins, value=value)

            # Get chi for all nuclides in the domain
            elif nuclides == 'all':
                nuclides = self.get_all_nuclides()
                xs = self.xs_tally.get_values(filters=filters,
                                              filter_bins=filter_bins,
                                              nuclides=nuclides, value=value)

            # Get chi for user-specified nuclides in the domain
            else:
                cv.check_iterable_type('nuclides', nuclides, basestring)
                xs = self.xs_tally.get_values(filters=filters,
                                              filter_bins=filter_bins,
                                              nuclides=nuclides, value=value)

        # If chi was computed as an average of nuclides in the domain
        else:
            xs = self.xs_tally.get_values(filters=filters,
                                          filter_bins=filter_bins, value=value)

        # Reverse data if user requested increasing energy groups since
        # tally data is stored in order of increasing energies
        if order_groups == 'increasing':

            # Reshape tally data array with separate axes for domain and energy
            if groups == 'all':
                num_groups = self.num_groups
            else:
                num_groups = len(groups)
            num_subdomains = xs.shape[0] / num_groups
            new_shape = (num_subdomains, num_groups) + xs.shape[1:]
            xs = np.reshape(xs, new_shape)

            # Reverse energies to align with increasing energy groups
            xs = xs[:, ::-1, :]

            # Eliminate trivial dimensions
            xs = np.squeeze(xs)
            xs = np.atleast_1d(xs)

        xs = np.nan_to_num(xs)
        return xs

    def get_pandas_dataframe(self, groups='all', nuclides='all',
                             xs_type='macro', summary=None):
        """Build a Pandas DataFrame for the MGXS data.

        This method leverages the Tally.get_pandas_dataframe(...) method, but
        renames the columns with terminology appropriate for cross section data.

        Parameters
        ----------
        groups : Iterable of Integral or 'all'
            Energy groups of interest. Defaults to 'all'.
        nuclides : Iterable of str or 'all' or 'sum'
            The nuclides of the cross-sections to include in the dataframe. This
            may be a list of nuclide name strings (e.g., ['U-235', 'U-238']).
            The special string 'all' will include the cross sections for all
            nuclides in the spatial domain. The special string 'sum' will
            include the cross sections summed over all nuclides. Defaults to
            'all'.
        xs_type: {'macro', 'micro'}
            Return macro or micro cross section in units of cm^-1 or barns.
            Defaults to 'macro'.
        summary : None or Summary
            An optional Summary object to be used to construct columns for
            distribcell tally filters (default is None). The geometric
            information in the Summary object is embedded into a multi-index
            column with a geometric "path" to each distribcell intance.
            NOTE: This option requires the OpenCG Python package.

        Returns
        -------
        pandas.DataFrame
            A Pandas DataFrame for the cross section data.

        Raises
        ------
        ValueError
            When this method is called before the multi-group cross section is
            computed from tally data.

        """

        # Build the dataframe using the parent class method
        df = super(ChiDelayed, self).get_pandas_dataframe(groups, nuclides,
                                                          xs_type, summary)

        # If user requested micro cross sections, multiply by the atom
        # densities to cancel out division made by the parent class method
        if xs_type == 'micro':
            if self.by_nuclide:
                densities = self.get_nuclide_densities(nuclides)
            else:
                densities = self.get_nuclide_densities('sum')
            tile_factor = df.shape[0] / len(densities)
            df['mean'] *= np.tile(densities, tile_factor)
            df['std. dev.'] *= np.tile(densities, tile_factor)

        return df


class ChiPrompt(MGXS):
    """The prompt-neutron fission spectrum."""

    def __init__(self, domain=None, domain_type=None,
                 groups=None, by_nuclide=False, name=''):
        super(ChiPrompt, self).__init__(domain, domain_type, groups,
                                         by_nuclide, name)
        self._rxn_type = 'chi-prompt'

    def create_tallies(self):
        """Construct the OpenMC tallies needed to compute this cross section.

        This method constructs two analog tallies to compute 'delayed-nu-fission'
        reaction rates with 'energy' and 'energyout' filters in the spatial
        domain and energy groups of interest.

        """

        # Create a list of scores for each Tally to be created
        scores = ['delayed-nu-fission', 'delayed-nu-fission',
                  'nu-fission', 'nu-fission']
        estimator = 'analog'
        keys = ['delayed-nu-fission-in', 'delayed-nu-fission-out',
                'nu-fission-in', 'nu-fission-out']

        # Create the non-domain specific Filters for the Tallies
        group_edges = self.energy_groups.group_edges
        energyout = openmc.Filter('energyout', group_edges)
        energyin = openmc.Filter('energy', [group_edges[0], group_edges[-1]])
        filters = [[energyin], [energyout], [energyin], [energyout]]

        # Intialize the Tallies
        super(ChiPrompt, self).create_tallies(scores, filters, keys, estimator)

    def compute_xs(self):
        """Computes prompt chi fission spectrum using OpenMC tally arithmetic."""

        # Retrieve the fission production tallies
        delayed_nu_fission_in = self.tallies['delayed-nu-fission-in']
        delayed_nu_fission_out = self.tallies['delayed-nu-fission-out']
        nu_fission_in = self.tallies['nu-fission-in']
        nu_fission_out = self.tallies['nu-fission-out']

        # Remove coarse energy filter to keep it out of tally arithmetic
        energy_filter_d = delayed_nu_fission_in.find_filter('energy')
        delayed_nu_fission_in.remove_filter(energy_filter_d)
        energy_filter = nu_fission_in.find_filter('energy')
        nu_fission_in.remove_filter(energy_filter)

        # Compute delayed chi
        self._xs_tally = (nu_fission_out - delayed_nu_fission_out) \
                         / (nu_fission_in - delayed_nu_fission_in)

        # Add the coarse energy filter back to the nu-fission tally
        delayed_nu_fission_in.add_filter(energy_filter_d)
        nu_fission_in.add_filter(energy_filter)

        super(ChiPrompt, self).compute_xs()

    def get_xs(self, groups='all', subdomains='all', nuclides='all',
               xs_type='macro', order_groups='increasing', value='mean'):
        """Returns an array of the delayed-neutron fission spectrum.

        This method constructs a 2D NumPy array for the requested multi-group
        cross section data data for one or more energy groups and subdomains.

        Parameters
        ----------
        groups : Iterable of Integral or 'all'
            Energy groups of interest. Defaults to 'all'.
        subdomains : Iterable of Integral or 'all'
            Subdomain IDs of interest. Defaults to 'all'.
        nuclides : Iterable of str or 'all' or 'sum'
            A list of nuclide name strings (e.g., ['U-235', 'U-238']). The
            special string 'all' will return the cross sections for all nuclides
            in the spatial domain. The special string 'sum' will return the
            cross section summed over all nuclides. Defaults to 'all'.
        xs_type: {'macro', 'micro'}
            This parameter is not relevant for chi but is included here to
            mirror the parent MGXS.get_xs(...) class method
        order_groups: {'increasing', 'decreasing'}
            Return the cross section indexed according to increasing or
            decreasing energy groups (decreasing or increasing energies).
            Defaults to 'increasing'.
        value : str
            A string for the type of value to return - 'mean', 'std_dev', or
            'rel_err' are accepted. Defaults to 'mean'.

        Returns
        -------
        ndarray
            A NumPy array of the multi-group cross section indexed in the order
            each group, subdomain and nuclide is listed in the parameters.

        Raises
        ------
        ValueError
            When this method is called before the multi-group cross section is
            computed from tally data.

        """

        if self.xs_tally is None:
            msg = 'Unable to get cross section since it has not been computed'
            raise ValueError(msg)

        cv.check_value('value', value, ['mean', 'std_dev', 'rel_err'])
        cv.check_value('xs_type', xs_type, ['macro', 'micro'])

        filters = []
        filter_bins = []

        # Construct a collection of the domain filter bins
        if subdomains != 'all':
            cv.check_iterable_type('subdomains', subdomains, Integral)
            for subdomain in subdomains:
                filters.append(self.domain_type)
                filter_bins.append((subdomain,))

        # Construct list of energy group bounds tuples for all requested groups
        if groups != 'all':
            cv.check_iterable_type('groups', groups, Integral)
            for group in groups:
                filters.append('energyout')
                filter_bins.append((self.energy_groups.get_group_bounds(group),))

        # If chi was computed for each nuclide in the domain
        if self.by_nuclide:

            # Get the sum as the fission source weighted average chi for all
            # nuclides in the domain
            if nuclides == 'sum' or nuclides == ['sum']:

                # Retrieve the fission production tallies
                delayed_nu_fission_in = self.tallies['delayed-nu-fission-in']
                delayed_nu_fission_out = self.tallies['delayed-nu-fission-out']
                nu_fission_in = self.tallies['nu-fission-in']
                nu_fission_out = self.tallies['nu-fission-out']

                # Sum out all nuclides
                nuclides = self.get_all_nuclides()
                delayed_nu_fission_in = delayed_nu_fission_in.summation(nuclides=nuclides)
                delayed_nu_fission_out = delayed_nu_fission_out.summation(nuclides=nuclides)
                nu_fission_in = nu_fission_in.summation(nuclides=nuclides)
                nu_fission_out = nu_fission_out.summation(nuclides=nuclides)

                # Remove coarse energy filter to keep it out of tally arithmetic
                energy_filter_d = delayed_nu_fission_in.find_filter('energy')
                delayed_nu_fission_in.remove_filter(energy_filter_d)
                energy_filter = nu_fission_in.find_filter('energy')
                nu_fission_in.remove_filter(energy_filter)

                # Compute chi and store it as the xs_tally attribute so we can
                # use the generic get_xs(...) method
                xs_tally = (nu_fission_out - delayed_nu_fission_out) \
                           / (nu_fission_in - delayed_nu_fission_in)

                # Add the coarse energy filter back to the nu-fission tally
                delayed_nu_fission_in.add_filter(energy_filter_d)
                nu_fission_in.add_filter(energy_filter)

                xs = xs_tally.get_values(filters=filters,
                                         filter_bins=filter_bins, value=value)

            # Get chi for all nuclides in the domain
            elif nuclides == 'all':
                nuclides = self.get_all_nuclides()
                xs = self.xs_tally.get_values(filters=filters,
                                              filter_bins=filter_bins,
                                              nuclides=nuclides, value=value)

            # Get chi for user-specified nuclides in the domain
            else:
                cv.check_iterable_type('nuclides', nuclides, basestring)
                xs = self.xs_tally.get_values(filters=filters,
                                              filter_bins=filter_bins,
                                              nuclides=nuclides, value=value)

        # If chi was computed as an average of nuclides in the domain
        else:
            xs = self.xs_tally.get_values(filters=filters,
                                          filter_bins=filter_bins, value=value)

        # Reverse data if user requested increasing energy groups since
        # tally data is stored in order of increasing energies
        if order_groups == 'increasing':

            # Reshape tally data array with separate axes for domain and energy
            if groups == 'all':
                num_groups = self.num_groups
            else:
                num_groups = len(groups)
            num_subdomains = xs.shape[0] / num_groups
            new_shape = (num_subdomains, num_groups) + xs.shape[1:]
            xs = np.reshape(xs, new_shape)

            # Reverse energies to align with increasing energy groups
            xs = xs[:, ::-1, :]

            # Eliminate trivial dimensions
            xs = np.squeeze(xs)
            xs = np.atleast_1d(xs)

        xs = np.nan_to_num(xs)
        return xs

    def get_pandas_dataframe(self, groups='all', nuclides='all',
                             xs_type='macro', summary=None):
        """Build a Pandas DataFrame for the MGXS data.

        This method leverages the Tally.get_pandas_dataframe(...) method, but
        renames the columns with terminology appropriate for cross section data.

        Parameters
        ----------
        groups : Iterable of Integral or 'all'
            Energy groups of interest. Defaults to 'all'.
        nuclides : Iterable of str or 'all' or 'sum'
            The nuclides of the cross-sections to include in the dataframe. This
            may be a list of nuclide name strings (e.g., ['U-235', 'U-238']).
            The special string 'all' will include the cross sections for all
            nuclides in the spatial domain. The special string 'sum' will
            include the cross sections summed over all nuclides. Defaults to
            'all'.
        xs_type: {'macro', 'micro'}
            Return macro or micro cross section in units of cm^-1 or barns.
            Defaults to 'macro'.
        summary : None or Summary
            An optional Summary object to be used to construct columns for
            distribcell tally filters (default is None). The geometric
            information in the Summary object is embedded into a multi-index
            column with a geometric "path" to each distribcell intance.
            NOTE: This option requires the OpenCG Python package.

        Returns
        -------
        pandas.DataFrame
            A Pandas DataFrame for the cross section data.

        Raises
        ------
        ValueError
            When this method is called before the multi-group cross section is
            computed from tally data.

        """

        # Build the dataframe using the parent class method
        df = super(ChiPrompt, self).get_pandas_dataframe(groups, nuclides,
                                                         xs_type, summary)

        # If user requested micro cross sections, multiply by the atom
        # densities to cancel out division made by the parent class method
        if xs_type == 'micro':
            if self.by_nuclide:
                densities = self.get_nuclide_densities(nuclides)
            else:
                densities = self.get_nuclide_densities('sum')
            tile_factor = df.shape[0] / len(densities)
            df['mean'] *= np.tile(densities, tile_factor)
            df['std. dev.'] *= np.tile(densities, tile_factor)

        return df
