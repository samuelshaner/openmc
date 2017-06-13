from collections import OrderedDict
from copy import deepcopy
from numbers import Real, Integral
import warnings
from xml.etree import ElementTree as ET

from six import string_types
import numpy as np

import openmc
import openmc.data
import openmc.checkvalue as cv
from openmc.clean_xml import sort_xml_elements, clean_xml_indentation


# A static variable for auto-generated Channel IDs
AUTO_CHANNEL_ID = 10000


def reset_auto_channel_id():
    """Reset counter for auto-generated channel IDs."""
    global AUTO_CHANNEL_ID
    AUTO_CHANNEL_ID = 10000


class CoolantChannel(object):
    """A coolant channel contains the interfacial components needed to perform TH feedback.

    Coolant channels are created by a Geometry object and will contain the info
    needed to perform TH feedback with Cobra TF.

    Parameters
    ----------
    channel_id : int, optional
        Unique identifier for the channel. If not specified, an identifier will
        automatically be assigned.
    name : str, optional
        Name of the material. If not specified, the name will be the empty
        string.

    Attributes
    ----------
    id : int
        Unique identifier for the channel
    cell_offsets : dict
        Dict of with the cell objects as keys and the cell offsets as values.
    power_tallies : Iterable of openmc.Tally
        Iterable of distrib cell tallies that contain the reaction rates needed
        to computed the energy generation rate in each of the heated cells.
    coolant_cells : Iterable of openmc.Cell
        Iterable of the coolant cells in a channel.
    flow_area : Iterable of float
        Iterable of the flow area to neighboring channels in the six directions.

    """

    def __init__(self, channel_id=None, name=''):

        # Initialize class attributes
        self.id = channel_id
        self.name = name
        self._cell_offsets = {}
        self._power_tallies = []
        self._coolant_cells = []
        self._flow_area = np.zeros(6)

    def __eq__(self, other):
        if not isinstance(other, CoolantChannel):
            return False
        elif self.id != other.id:
            return False
        elif self.name != other.name:
            return False
        elif self._cell_offsets != other._cell_offsets:
            return False
        elif self._power_tallies != other._power_tallies:
            return False
        elif self._coolant_cells != other._coolant_cells:
            return False
        elif self._flow_area != other._flow_area:
            return False
        else:
            return True

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        string = 'Coolant Channel\n'
        string += '{: <16}=\t{}\n'.format('\tID', self._id)
        string += '{: <16}=\t{}\n'.format('\tName', self._name)

        string += '{: <16}\n'.format('\tCell Offsets')

        for key,value in self._cell_offsets.items():
            string += 'Cell offset:  ({}, {})\n'.format(key.id, value)

        string += '{: <16}\n'.format('\tPower Tallies')

        for tally in self._power_tallies:
            string += tally + '\n'

        string += '{: <16}\n'.format('\tCoolant Cells')

        for cell in self._coolant_cells:
            string += 'Cell:  {}\n'.format(cell)

        string += '{: <16}\n'.format('\tFlow Area')

        for i,area in enumerate(self._flow_area):
            string += 'Surface {} flow area:  {}\n'.format(i, area)

        return string

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def cell_offsets(self):
        return self._cell_offsets

    @property
    def power_tallies(self):
        return self._power_tallies

    @property
    def coolant_cells(self):
        return self._coolant_cells

    @property
    def flow_area(self):
        return self._flow_area

    @id.setter
    def id(self, channel_id):

        if channel_id is None:
            global AUTO_CHANNEL_ID
            self._id = AUTO_CHANNEL_ID
            AUTO_CHANNEL_ID += 1
        else:
            cv.check_type('channel ID', channel_id, Integral)
            cv.check_greater_than('channel ID', channel_id, 0, equality=True)
            self._id = channel_id

    @name.setter
    def name(self, name):
        if name is not None:
            cv.check_type('name for Coolant Channel ID="{}"'.format(self._id),
                          name, string_types)
            self._name = name
        else:
            self._name = ''

    def add_cell(self, cell, offset, coolant=False):
        """Add a cell to the coolant channel

        Parameters
        ----------
        cell : openmc.Cell
            Cell to add
        cell_offset : int
            Distrib cell offset
        coolant : bool, optional
            Bool indicating whether this is a coolant cell

        """

        if not isinstance(cell, openmc.Cell):
            msg = 'Unable to add a Cell to Coolant Channel ID="{}" with a ' \
                  'non-Cell value "{}"'.format(self._id, cell)
            raise ValueError(msg)

        elif not isinstance(offset, int):
            msg = 'Unable to add a Cell to Coolant Channel ID="{}" with a ' \
                  'non-integer cell offset "{}"'.format(self._id, offset)
            raise ValueError(msg)

        elif not isinstance(coolant, bool):
            msg = 'Unable to add a Cell to Coolant Channel ID="{}" with a ' \
                  'non-bool coolant indicator "{}"'.format(self._id, coolant)
            raise ValueError(msg)

        cv.check_greater_than('coolant channel cell offset', offset, 0, True)

        self._cell_offsets[cell] = offset

        if coolant:
            self._coolant_cells.append(cell.id)

    def add_power_tally(self, tally):
        """Add a power tally to the coolant channel

        Parameters
        ----------
        tally : openmc.Tally
            Power tally to add

        """

        if not isinstance(tally, openmc.Tally):
            msg = 'Unable to add a Power Tally to Coolant Channel ID="{}" ' \
                  'with a non-Tally value "{}"'.format(self._id, tally)
            raise ValueError(msg)

        self._power_tallies.append(tally)

    def set_flow_area(self, surface, area):
        """Set the flow area of a surface

        Parameters
        ----------
        surface : int
            The integer id of the surface. The ids for the surface follow the
            ordered used for surfaces/lattice face ordering found in
            constants.F90.
        area : float
            The flow area

        """

        if not isinstance(surface, int):
            msg = 'Unable to set flow area for Coolant Channel ID="{}" ' \
                  'with non-int surface "{}"'.format(self._id, surface)
            raise ValueError(msg)
        if not isinstance(area, Real):
            msg = 'Unable to set flow area for Coolant Channel ID="{}" ' \
                  'with non-Real area "{}"'.format(self._id, area)
            raise ValueError(msg)

        cv.check_less_than('flow area surface', surface, 6)
        cv.check_greater_than('flow area surface', surface, 0, True)
        cv.check_greater_than('flow area', area, 0., True)

        self._flow_area[surface] = area

    def contains_cell(self, cell, offset):
        """Check if this channel contains a cell with the given offset

        Parameters
        ----------
        cell : openmc.Cell
            Cell to check
        cell_offset : int
            Distrib cell offset

        Returns
        -------
        bool
           Whether this channel contains the cell with the given offset

        """

        if (cell, offset) in self._cell_offsets.items():
            return True
        else:
            return False
