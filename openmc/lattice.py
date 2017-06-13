from __future__ import division

from abc import ABCMeta
from collections import OrderedDict, Iterable
from copy import deepcopy
from math import sqrt, floor
from numbers import Real, Integral
from xml.etree import ElementTree as ET

from six import add_metaclass, string_types
import numpy as np

import openmc.checkvalue as cv
import openmc


@add_metaclass(ABCMeta)
class Lattice(object):
    """A repeating structure wherein each element is a universe.

    Parameters
    ----------
    lattice_id : int, optional
        Unique identifier for the lattice. If not specified, an identifier will
        automatically be assigned.
    name : str, optional
        Name of the lattice. If not specified, the name is the empty string.

    Attributes
    ----------
    id : int
        Unique identifier for the lattice
    name : str
        Name of the lattice
    pitch : Iterable of float
        Pitch of the lattice in each direction in cm
    outer : openmc.Universe
        A universe to fill all space outside the lattice
    universes : Iterable of Iterable of openmc.Universe
        A two- or three-dimensional list/array of universes filling each element
        of the lattice
    channelizeable : bool
        A boolean akin to the fissionable property of materials indicating
        whether it is possible to form channels with this lattice. Default is
        False.
    """
    def __init__(self, lattice_id=None, name=''):
        # Initialize Lattice class attributes
        self.id = lattice_id
        self.name = name
        self._pitch = None
        self._outer = None
        self._universes = None
        self._channelizeable = False

    def __eq__(self, other):
        if not isinstance(other, Lattice):
            return False
        elif self.id != other.id:
            return False
        elif self.name != other.name:
            return False
        elif self.channelizeable != other.channelizeable:
            return False
        elif np.any(self.pitch != other.pitch):
            return False
        elif self.outer != other.outer:
            return False
        elif np.any(self.universes != other.universes):
            return False
        else:
            return True

    def __ne__(self, other):
        return not self == other

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def pitch(self):
        return self._pitch

    @property
    def outer(self):
        return self._outer

    @property
    def universes(self):
        return self._universes

    @property
    def channelizeable(self):
        return self._channelizeable

    @id.setter
    def id(self, lattice_id):
        if lattice_id is None:
            self._id = openmc.universe.AUTO_UNIVERSE_ID
            openmc.universe.AUTO_UNIVERSE_ID += 1
        else:
            cv.check_type('lattice ID', lattice_id, Integral)
            cv.check_greater_than('lattice ID', lattice_id, 0, equality=True)
            self._id = lattice_id

    @name.setter
    def name(self, name):
        if name is not None:
            cv.check_type('lattice name', name, string_types)
            self._name = name
        else:
            self._name = ''

    @channelizeable.setter
    def channelizeable(self, channelizeable):
        cv.check_type('channelizeable', channelizeable, bool)
        self._channelizeable = channelizeable

    @outer.setter
    def outer(self, outer):
        cv.check_type('outer universe', outer, openmc.Universe)
        self._outer = outer

    @staticmethod
    def from_hdf5(group, universes):
        """Create lattice from HDF5 group

        Parameters
        ----------
        group : h5py.Group
            Group in HDF5 file
        universes : dict
            Dictionary mapping universe IDs to instances of
            :class:`openmc.Universe`.

        Returns
        -------
        openmc.Lattice
            Instance of lattice subclass

        """
        lattice_id = int(group.name.split('/')[-1].lstrip('lattice '))
        name = group['name'].value.decode() if 'name' in group else ''
        lattice_type = group['type'].value.decode()

        if lattice_type == 'rectangular':
            dimension = group['dimension'][...]
            lower_left = group['lower_left'][...]
            pitch = group['pitch'][...]
            outer = group['outer'].value
            universe_ids = group['universes'][...]

            # Create the Lattice
            lattice = openmc.RectLattice(lattice_id, name)
            lattice.lower_left = lower_left
            lattice.pitch = pitch

            # If the Universe specified outer the Lattice is not void
            if outer >= 0:
                lattice.outer = universes[outer]

            # Build array of Universe pointers for the Lattice
            uarray = np.empty(universe_ids.shape, dtype=openmc.Universe)

            for z in range(universe_ids.shape[0]):
                for y in range(universe_ids.shape[1]):
                    for x in range(universe_ids.shape[2]):
                        uarray[z, y, x] = universes[universe_ids[z, y, x]]

            # Use 2D NumPy array to store lattice universes for 2D lattices
            if len(dimension) == 2:
                uarray = np.squeeze(uarray)
                uarray = np.atleast_2d(uarray)

            # Set the universes for the lattice
            lattice.universes = uarray

        elif lattice_type == 'hexagonal':
            n_rings = group['n_rings'].value
            n_axial = group['n_axial'].value
            center = group['center'][...]
            pitch = group['pitch'][...]
            outer = group['outer'].value

            universe_ids = group['universes'][...]

            # Create the Lattice
            lattice = openmc.HexLattice(lattice_id, name)
            lattice.center = center
            lattice.pitch = pitch

            # If the Universe specified outer the Lattice is not void
            if outer >= 0:
                lattice.outer = universes[outer]

            # Build array of Universe pointers for the Lattice.  Note that
            # we need to convert between the HDF5's square array of
            # (x, alpha, z) to the Python API's format of a ragged nested
            # list of (z, ring, theta).
            uarray = []
            for z in range(n_axial):
                # Add a list for this axial level.
                uarray.append([])
                x = n_rings - 1
                a = 2*n_rings - 2
                for r in range(n_rings - 1, 0, -1):
                    # Add a list for this ring.
                    uarray[-1].append([])

                    # Climb down the top-right.
                    for i in range(r):
                        uarray[-1][-1].append(universe_ids[z, a, x])
                        x += 1
                        a -= 1

                    # Climb down the right.
                    for i in range(r):
                        uarray[-1][-1].append(universe_ids[z, a, x])
                        a -= 1

                    # Climb down the bottom-right.
                    for i in range(r):
                        uarray[-1][-1].append(universe_ids[z, a, x])
                        x -= 1

                    # Climb up the bottom-left.
                    for i in range(r):
                        uarray[-1][-1].append(universe_ids[z, a, x])
                        x -= 1
                        a += 1

                    # Climb up the left.
                    for i in range(r):
                        uarray[-1][-1].append(universe_ids[z, a, x])
                        a += 1

                    # Climb up the top-left.
                    for i in range(r):
                        uarray[-1][-1].append(universe_ids[z, a, x])
                        x += 1

                    # Move down to the next ring.
                    a -= 1

                    # Convert the ids into Universe objects.
                    uarray[-1][-1] = [universes[u_id]
                                      for u_id in uarray[-1][-1]]

                # Handle the degenerate center ring separately.
                u_id = universe_ids[z, a, x]
                uarray[-1].append([universes[u_id]])

            # Add the universes to the lattice.
            if len(pitch) == 2:
                # Lattice is 3D
                lattice.universes = uarray
            else:
                # Lattice is 2D; extract the only axial level
                lattice.universes = uarray[0]

        return lattice

    def get_unique_universes(self):
        """Determine all unique universes in the lattice

        Returns
        -------
        universes : collections.OrderedDict
            Dictionary whose keys are universe IDs and values are
            :class:`openmc.Universe` instances

        """

        univs = OrderedDict()
        for k in range(len(self._universes)):
            for j in range(len(self._universes[k])):
                if isinstance(self._universes[k][j], openmc.Universe):
                    u = self._universes[k][j]
                    univs[u._id] = u
                else:
                    for i in range(len(self._universes[k][j])):
                        u = self._universes[k][j][i]
                        assert isinstance(u, openmc.Universe)
                        univs[u._id] = u

        if self.outer is not None:
            univs[self.outer._id] = self.outer

        return univs

    def get_nuclides(self):
        """Returns all nuclides in the lattice

        Returns
        -------
        nuclides : list of str
            List of nuclide names

        """

        nuclides = []

        # Get all unique Universes contained in each of the lattice cells
        unique_universes = self.get_unique_universes()

        # Append all Universes containing each cell to the dictionary
        for universe in unique_universes.values():
            for nuclide in universe.get_nuclides():
                if nuclide not in nuclides:
                    nuclides.append(nuclide)

        return nuclides

    def get_all_cells(self):
        """Return all cells that are contained within the lattice

        Returns
        -------
        cells : collections.OrderedDict
            Dictionary whose keys are cell IDs and values are :class:`Cell`
            instances

        """

        cells = OrderedDict()
        unique_universes = self.get_unique_universes()

        for universe_id, universe in unique_universes.items():
            cells.update(universe.get_all_cells())

        return cells

    def get_all_materials(self):
        """Return all materials that are contained within the lattice

        Returns
        -------
        materials : collections.OrderedDict
            Dictionary whose keys are material IDs and values are
            :class:`Material` instances

        """

        materials = OrderedDict()

        # Append all Cells in each Cell in the Universe to the dictionary
        cells = self.get_all_cells()
        for cell_id, cell in cells.items():
            materials.update(cell.get_all_materials())

        return materials

    def get_all_universes(self):
        """Return all universes that are contained within the lattice

        Returns
        -------
        universes : collections.OrderedDict
            Dictionary whose keys are universe IDs and values are
            :class:`Universe` instances

        """

        # Initialize a dictionary of all Universes contained by the Lattice
        # in each nested Universe level
        all_universes = OrderedDict()

        # Get all unique Universes contained in each of the lattice cells
        unique_universes = self.get_unique_universes()

        # Add the unique Universes filling each Lattice cell
        all_universes.update(unique_universes)

        # Append all Universes containing each cell to the dictionary
        for universe_id, universe in unique_universes.items():
            all_universes.update(universe.get_all_universes())

        return all_universes

    def get_universe(self, idx):
        r"""Return universe corresponding to a lattice element index

        Parameters
        ----------
        idx : Iterable of int
            Lattice element indices. For a rectangular lattice, the indices are
            given in the :math:`(x,y)` or :math:`(x,y,z)` coordinate system. For
            hexagonal lattices, they are given in the :math:`x,\alpha` or
            :math:`x,\alpha,z` coordinate systems.

        Returns
        -------
        openmc.Universe
            Universe with given indices

        """
        idx_u = self.get_universe_index(idx)
        if self.ndim == 2:
            return self.universes[idx_u[0]][idx_u[1]]
        else:
            return self.universes[idx_u[0]][idx_u[1]][idx_u[2]]

    def find(self, point):
        """Find cells/universes/lattices which contain a given point

        Parameters
        ----------
        point : 3-tuple of float
            Cartesian coordinates of the point

        Returns
        -------
        list
            Sequence of universes, cells, and lattices which are traversed to
            find the given point

        """
        idx, p = self.find_element(point)
        if self.is_valid_index(idx):
            u = self.get_universe(idx)
        else:
            if self.outer is not None:
                u = self.outer
            else:
                return []
        return [(self, idx)] + u.find(p)

    def clone(self, memo=None):
        """Create a copy of this lattice with a new unique ID, and clones
        all universes within this lattice.

        Parameters
        ----------
        memo : dict or None
            A nested dictionary of previously cloned objects. This parameter
            is used internally and should not be specified by the user.

        Returns
        -------
        clone : openmc.Lattice
            The clone of this lattice

        """

        if memo is None:
            memo = {}

        # If no nemoize'd clone exists, instantiate one
        if self not in memo:
            clone = deepcopy(self)
            clone.id = None

            if self.outer is not None:
                clone.outer = self.outer.clone(memo)

            # Assign universe clones to the lattice clone
            for i in self.indices:
                if isinstance(self, RectLattice):
                    clone.universes[i] = self.universes[i].clone(memo)
                else:
                    if self.ndim == 2:
                        clone.universes[i[0]][i[1]] = \
                            self.universes[i[0]][i[1]].clone(memo)
                    else:
                        clone.universes[i[0]][i[1]][i[2]] = \
                            self.universes[i[0]][i[1]][i[2]].clone(memo)

            # Memoize the clone
            memo[self] = clone

        return memo[self]


class RectLattice(Lattice):
    """A lattice consisting of rectangular prisms.

    To completely define a rectangular lattice, the
    :attr:`RectLattice.lower_left` :attr:`RectLattice.pitch`,
    :attr:`RectLattice.outer`, and :attr:`RectLattice.universes` properties need
    to be set.

    Most methods for this class use a natural indexing scheme wherein elements
    are assigned an index corresponding to their position relative to the
    (x,y,z) axes in a Cartesian coordinate system, i.e., an index of (0,0,0) in
    the lattice gives the element whose x, y, and z coordinates are the
    smallest. However, note that when universes are assigned to lattice elements
    using the :attr:`RectLattice.universes` property, the array indices do not
    correspond to natural indices.

    Parameters
    ----------
    lattice_id : int, optional
        Unique identifier for the lattice. If not specified, an identifier will
        automatically be assigned.
    name : str, optional
        Name of the lattice. If not specified, the name is the empty string.

    Attributes
    ----------
    id : int
        Unique identifier for the lattice
    name : str
        Name of the lattice
    pitch : Iterable of float
        Pitch of the lattice in the x, y, and (if applicable) z directions in
        cm.
    outer : openmc.Universe
        A universe to fill all space outside the lattice
    universes : Iterable of Iterable of openmc.Universe
        A two- or three-dimensional list/array of universes filling each element
        of the lattice. The first dimension corresponds to the z-direction (if
        applicable), the second dimension corresponds to the y-direction, and
        the third dimension corresponds to the x-direction. Note that for the
        y-direction, a higher index corresponds to a lower physical
        y-value. Each z-slice in the array can be thought of as a top-down view
        of the lattice.
    lower_left : Iterable of float
        The Cartesian coordinates of the lower-left corner of the lattice. If
        the lattice is two-dimensional, only the x- and y-coordinates are
        specified.
    indices : list of tuple
        A list of all possible (z,y,x) or (y,x) lattice element indices. These
        indices correspond to indices in the :attr:`RectLattice.universes`
        property.
    ndim : int
        The number of dimensions of the lattice
    shape : Iterable of int
        An array of two or three integers representing the number of lattice
        cells in the x- and y- (and z-) directions, respectively.

    """

    def __init__(self, lattice_id=None, name=''):
        super(RectLattice, self).__init__(lattice_id, name)

        # Initialize Lattice class attributes
        self._lower_left = None

    def __eq__(self, other):
        if not isinstance(other, RectLattice):
            return False
        elif not super(RectLattice, self).__eq__(other):
            return False
        elif self.shape != other.shape:
            return False
        elif np.any(self.lower_left != other.lower_left):
            return False
        else:
            return True

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        string = 'RectLattice\n'
        string += '{0: <16}{1}{2}\n'.format('\tID', '=\t', self._id)
        string += '{0: <16}{1}{2}\n'.format('\tName', '=\t', self._name)
        string += '{0: <16}{1}{2}\n'.format('\tShape', '=\t',
                                            self.shape)
        string += '{0: <16}{1}{2}\n'.format('\tLower Left', '=\t',
                                            self._lower_left)
        string += '{0: <16}{1}{2}\n'.format('\tPitch', '=\t', self._pitch)

        if self._outer is not None:
            string += '{0: <16}{1}{2}\n'.format('\tOuter', '=\t',
                                                self._outer._id)
        else:
            string += '{0: <16}{1}{2}\n'.format('\tOuter', '=\t',
                                                self._outer)

        string += '{0: <16}\n'.format('\tUniverses')

        # Lattice nested Universe IDs - column major for Fortran
        for i, universe in enumerate(np.ravel(self._universes)):
            string += '{0} '.format(universe._id)

            # Add a newline character every time we reach end of row of cells
            if (i+1) % self.shape[0] == 0:
                string += '\n'

        string = string.rstrip('\n')

        return string

    @property
    def indices(self):
        if self.ndim == 2:
            return list(np.broadcast(*np.ogrid[
                :self.shape[1], :self.shape[0]]))
        else:
            return list(np.broadcast(*np.ogrid[
                :self.shape[2], :self.shape[1], :self.shape[0]]))

    @property
    def _natural_indices(self):
        """Iterate over all possible (x,y) or (x,y,z) lattice element indices.

        This property is used when constructing distributed cell and material
        paths. Most importantly, the iteration order matches that used on the
        Fortran side.

        """
        if self.ndim == 2:
            nx, ny = self.shape
            return np.broadcast(*np.ogrid[:nx, :ny])
        else:
            nx, ny, nz = self.shape
            return np.broadcast(*np.ogrid[:nx, :ny, :nz])

    @property
    def lower_left(self):
        return self._lower_left

    @property
    def ndim(self):
        return len(self.pitch)

    @property
    def shape(self):
        return self._universes.shape[::-1]

    @lower_left.setter
    def lower_left(self, lower_left):
        cv.check_type('lattice lower left corner', lower_left, Iterable, Real)
        cv.check_length('lattice lower left corner', lower_left, 2, 3)
        self._lower_left = lower_left

    @Lattice.pitch.setter
    def pitch(self, pitch):
        cv.check_type('lattice pitch', pitch, Iterable, Real)
        cv.check_length('lattice pitch', pitch, 2, 3)
        for dim in pitch:
            cv.check_greater_than('lattice pitch', dim, 0.0)
        self._pitch = pitch

    @Lattice.universes.setter
    def universes(self, universes):
        cv.check_iterable_type('lattice universes', universes, openmc.Universe,
                               min_depth=2, max_depth=3)
        self._universes = np.asarray(universes)

    def find_element(self, point):
        """Determine index of lattice element and local coordinates for a point

        Parameters
        ----------
        point : Iterable of float
            Cartesian coordinates of point

        Returns
        -------
        2- or 3-tuple of int
            A tuple of the corresponding (x,y,z) lattice element indices
        3-tuple of float
            Carestian coordinates of the point in the corresponding lattice
            element coordinate system

        """
        ix = floor((point[0] - self.lower_left[0])/self.pitch[0])
        iy = floor((point[1] - self.lower_left[1])/self.pitch[1])
        if self.ndim == 2:
            idx = (ix, iy)
        else:
            iz = floor((point[2] - self.lower_left[2])/self.pitch[2])
            idx = (ix, iy, iz)
        return idx, self.get_local_coordinates(point, idx)

    def get_local_coordinates(self, point, idx):
        """Determine local coordinates of a point within a lattice element

        Parameters
        ----------
        point : Iterable of float
            Cartesian coordinates of point
        idx : Iterable of int
            (x,y,z) indices of lattice element. If the lattice is 2D, the z
            index can be omitted.

        Returns
        -------
        3-tuple of float
            Cartesian coordinates of point in the lattice element coordinate
            system

        """
        x = point[0] - (self.lower_left[0] + (idx[0] + 0.5)*self.pitch[0])
        y = point[1] - (self.lower_left[1] + (idx[1] + 0.5)*self.pitch[1])
        if self.ndim == 2:
            z = point[2]
        else:
            z = point[2] - (self.lower_left[2] + (idx[2] + 0.5)*self.pitch[2])
        return (x, y, z)

    def get_universe_index(self, idx):
        """Return index in the universes array corresponding to a lattice element index

        Parameters
        ----------
        idx : Iterable of int
            Lattice element indices in the :math:`(x,y,z)` coordinate system

        Returns
        -------
        2- or 3-tuple of int
            Indices used when setting the :attr:`RectLattice.universes` property

        """
        max_y = self.shape[1] - 1
        if self.ndim == 2:
            x, y = idx
            return (max_y - y, x)
        else:
            x, y, z = idx
            return (z, max_y - y, x)

    def is_valid_index(self, idx):
        """Determine whether lattice element index is within defined range

        Parameters
        ----------
        idx : Iterable of int
            Lattice element indices in the :math:`(x,y,z)` coordinate system

        Returns
        -------
        bool
            Whether index is valid

        """
        if self.ndim == 2:
            return (0 <= idx[0] < self.shape[0] and
                    0 <= idx[1] < self.shape[1])
        else:
            return (0 <= idx[0] < self.shape[0] and
                    0 <= idx[1] < self.shape[1] and
                    0 <= idx[2] < self.shape[2])

    def create_xml_subelement(self, xml_element):

        # Determine if XML element already contains subelement for this Lattice
        path = './lattice[@id=\'{0}\']'.format(self._id)
        test = xml_element.find(path)

        # If the element does contain the Lattice subelement, then return
        if test is not None:
            return

        lattice_subelement = ET.Element("lattice")
        lattice_subelement.set("id", str(self._id))

        if len(self._name) > 0:
            lattice_subelement.set("name", str(self._name))

        # Export the Lattice cell pitch
        pitch = ET.SubElement(lattice_subelement, "pitch")
        pitch.text = ' '.join(map(str, self._pitch))

        # Export the Lattice outer Universe (if specified)
        if self._outer is not None:
            outer = ET.SubElement(lattice_subelement, "outer")
            outer.text = '{0}'.format(self._outer._id)
            self._outer.create_xml_subelement(xml_element)

        # Export Lattice cell dimensions
        dimension = ET.SubElement(lattice_subelement, "dimension")
        dimension.text = ' '.join(map(str, self.shape))

        # Export Lattice lower left
        lower_left = ET.SubElement(lattice_subelement, "lower_left")
        lower_left.text = ' '.join(map(str, self._lower_left))

        # Export the Lattice nested Universe IDs - column major for Fortran
        universe_ids = '\n'

        # 3D Lattices
        if self.ndim == 3:
            for z in range(self.shape[2]):
                for y in range(self.shape[1]):
                    for x in range(self.shape[0]):
                        universe = self._universes[z][y][x]

                        # Append Universe ID to the Lattice XML subelement
                        universe_ids += '{0} '.format(universe._id)

                        # Create XML subelement for this Universe
                        universe.create_xml_subelement(xml_element)

                    # Add newline character when we reach end of row of cells
                    universe_ids += '\n'

                # Add newline character when we reach end of row of cells
                universe_ids += '\n'

        # 2D Lattices
        else:
            for y in range(self.shape[1]):
                for x in range(self.shape[0]):
                    universe = self._universes[y][x]

                    # Append Universe ID to Lattice XML subelement
                    universe_ids += '{0} '.format(universe._id)

                    # Create XML subelement for this Universe
                    universe.create_xml_subelement(xml_element)

                # Add newline character when we reach end of row of cells
                universe_ids += '\n'

        # Remove trailing newline character from Universe IDs string
        universe_ids = universe_ids.rstrip('\n')

        universes = ET.SubElement(lattice_subelement, "universes")
        universes.text = universe_ids

        # Append the XML subelement for this Lattice to the XML element
        xml_element.append(lattice_subelement)

    def discretize_coolant_channels(self):
        """Create the array of coolant channels that make up the lattice"""

        # Skip this lattice if it is not channelizeable or if channels have
        # already been created
        if not self.channelizeable:
            return

        # Coolant channels can only be created if the universes array has been
        # set
        if self.universes is None:
            msg = 'Unable to create coolant channels since the universes array'\
                  ' has not been set'
            raise ValueError(msg)

        dims = len(np.array(self.universes).shape)
        if dims == 3:
            msg = 'Unable to create coolant channels for a geometry that ' \
                  'contains a 3D lattice'
            raise ValueError(msg)

        # Create a set of the universes array
        univs = set(self.universes.flatten())

        # Discretize each unique universe
        for univ in univs:

            # Skip if universe has already been channelized
            if univ.channelized:
                return

            # Create a new cell to fill the entire universe
            master_cell = openmc.Cell()

            # Create a 2x2 lattice to fill the cell
            quad_lattice = openmc.RectLattice()
            master_cell.fill = quad_lattice
            quad_univs = []

            # Create sub universe and add all the univ's cells to it
            sub_univ = openmc.Universe()
            sub_univ.add_cells(univ.cells.values())

            # Loop over quadrants of lattice cell
            for quad in range(4):

                # Create new universes to fill the lattice
                quad_univ = openmc.Universe()
                quad_univs.append(quad_univ)

                # Compute signs for translating to the different quadrants
                x_sign = -(2 * (quad % 2) - 1)
                y_sign = (2 * (quad // 2 % 2) - 1)

                # Create translated cells to fill the universes
                quad_cell = openmc.Cell()
                trans = (x_sign*self.pitch[0]/4., y_sign*self.pitch[1]/4., 0.)
                quad_cell.translation = trans
                quad_univ.add_cell(quad_cell)
                quad_cell.fill = sub_univ

            # Set quad_lattice info
            quad_lattice.pitch = np.array(self.pitch[:2])/2.
            quad_lattice.lower_left = -np.array(self.pitch[:2])/2.
            quad_lattice.universes = np.array(quad_univs).reshape((2,2))

            # Remove all the cells from this universe
            univ.clear_cells()

            # Add the new cell to the universe
            univ.add_cell(master_cell)

            # Indicate that this universe has been channelized
            univ.channelized = True

    def create_coolant_channels(self, geometry, path):
        """Create the coolant channels for the lattice

        Parameters
        ----------
        geometry : openmc.Geometry
            The geometry
        path : str
            The path to this current cell

        Returns
        -------
        Iterable of Iterable of Iterable of openmc.CoolantChannel
            3D array of CoolantChannel objects that make up the lattice

        """

        if self.channelizeable:

            dims = self.universes.shape

            channels = []
            for y in range(dims[0] + 1):
                channels.append([])
                for x in range(dims[1] + 1):
                    channels[y].append(openmc.CoolantChannel())

            for y in range(dims[0]):
                for x,univ in enumerate(self.universes[::-1][y]):
                    cell = univ.cells.values()[0]
                    lat = cell.fill
                    new_path = '{}l{}({},{})->u{}->c{}->l{}'\
                               .format(path, self.id, x, y, univ.id, cell.id, lat.id)

                    for y1 in range(2):
                        for x1,sub_univ in enumerate(lat.universes[::-1][y1]):
                            sub_cell = sub_univ.cells.values()[0]
                            sub_sub_univ = sub_cell.fill
                            for cell in sub_sub_univ.cells.values():
                                sub_path = '{}({},{})->u{}->c{}->u{}->c{}'.\
                                           format(new_path, x1, y1, sub_univ.id,
                                                  sub_cell.id, sub_sub_univ.id,
                                                  cell.id)
                                offset = geometry.get_instances(sub_path)
                                channel = channels[y+y1][x+x1]
                                channel.cell_offsets[cell] = offset

            return [channels]

        else:

            all_channels = []
            dims = self.universes.shape
            for y in range(dims[0]):
                for x,univ in enumerate(self.universes[::-1][y]):
                    channels = univ.create_coolant_channels()
                    for channel in channels:
                        all_channels.append(channel)

            return all_channels


class HexLattice(Lattice):
    r"""A lattice consisting of hexagonal prisms.

    To completely define a hexagonal lattice, the :attr:`HexLattice.center`,
    :attr:`HexLattice.pitch`, :attr:`HexLattice.universes`, and
    :attr:`HexLattice.outer` properties need to be set.

    Most methods for this class use a natural indexing scheme wherein elements
    are assigned an index corresponding to their position relative to skewed
    :math:`(x,\alpha,z)` axes as described fully in
    :ref:`hexagonal_indexing`. However, note that when universes are assigned to
    lattice elements using the :attr:`HexLattice.universes` property, the array
    indices do not correspond to natural indices.

    Parameters
    ----------
    lattice_id : int, optional
        Unique identifier for the lattice. If not specified, an identifier will
        automatically be assigned.
    name : str, optional
        Name of the lattice. If not specified, the name is the empty string.

    Attributes
    ----------
    id : int
        Unique identifier for the lattice
    name : str
        Name of the lattice
    pitch : Iterable of float
        Pitch of the lattice in cm. The first item in the iterable specifies the
        pitch in the radial direction and, if the lattice is 3D, the second item
        in the iterable specifies the pitch in the axial direction.
    outer : openmc.Universe
        A universe to fill all space outside the lattice
    universes : Nested Iterable of openmc.Universe
        A two- or three-dimensional list/array of universes filling each element
        of the lattice. Each sub-list corresponds to one ring of universes and
        should be ordered from outermost ring to innermost ring. The universes
        within each sub-list are ordered from the "top" and proceed in a
        clockwise fashion. The :meth:`HexLattice.show_indices` method can be
        used to help figure out indices for this property.
    center : Iterable of float
        Coordinates of the center of the lattice. If the lattice does not have
        axial sections then only the x- and y-coordinates are specified
    indices : list of tuple
        A list of all possible (z,r,i) or (r,i) lattice element indices that are
        possible, where z is the axial index, r is in the ring index (starting
        from the outermost ring), and i is the index with a ring starting from
        the top and proceeding clockwise.
    num_rings : int
        Number of radial ring positions in the xy-plane
    num_axial : int
        Number of positions along the z-axis.

    """

    def __init__(self, lattice_id=None, name=''):
        super(HexLattice, self).__init__(lattice_id, name)

        # Initialize Lattice class attributes
        self._num_rings = None
        self._num_axial = None
        self._center = None

    def __eq__(self, other):
        if not isinstance(other, HexLattice):
            return False
        elif not super(HexLattice, self).__eq__(other):
            return False
        elif self.num_rings != other.num_rings:
            return False
        elif self.num_axial != other.num_axial:
            return False
        elif self.center != other.center:
            return False
        else:
            return True

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        string = 'HexLattice\n'
        string += '{0: <16}{1}{2}\n'.format('\tID', '=\t', self._id)
        string += '{0: <16}{1}{2}\n'.format('\tName', '=\t', self._name)
        string += '{0: <16}{1}{2}\n'.format('\t# Rings', '=\t', self._num_rings)
        string += '{0: <16}{1}{2}\n'.format('\t# Axial', '=\t', self._num_axial)
        string += '{0: <16}{1}{2}\n'.format('\tCenter', '=\t',
                                            self._center)
        string += '{0: <16}{1}{2}\n'.format('\tPitch', '=\t', self._pitch)

        if self._outer is not None:
            string += '{0: <16}{1}{2}\n'.format('\tOuter', '=\t',
                                                self._outer._id)
        else:
            string += '{0: <16}{1}{2}\n'.format('\tOuter', '=\t',
                                                self._outer)

        string += '{0: <16}\n'.format('\tUniverses')

        if self._num_axial is not None:
            slices = [self._repr_axial_slice(x) for x in self._universes]
            string += '\n'.join(slices)

        else:
            string += self._repr_axial_slice(self._universes)

        return string

    @property
    def num_rings(self):
        return self._num_rings

    @property
    def num_axial(self):
        return self._num_axial

    @property
    def center(self):
        return self._center

    @property
    def indices(self):
        if self.num_axial is None:
            return [(r, i) for r in range(self.num_rings)
                    for i in range(max(6*(self.num_rings - 1 - r), 1))]
        else:
            return [(z, r, i) for z in range(self.num_axial)
                    for r in range(self.num_rings)
                    for i in range(max(6*(self.num_rings - 1 - r), 1))]

    @property
    def _natural_indices(self):
        """Iterate over all possible (x,alpha) or (x,alpha,z) lattice element
        indices.

        This property is used when constructing distributed cell and material
        paths. Most importantly, the iteration order matches that used on the
        Fortran side.

        """
        r = self.num_rings
        if self.num_axial is None:
            for a in range(-r + 1, r):
                for x in range(-r + 1, r):
                    idx = (x, a)
                    if self.is_valid_index(idx):
                        yield idx
        else:
            for z in range(self.num_axial):
                for a in range(-r + 1, r):
                    for x in range(-r + 1, r):
                        idx = (x, a, z)
                        if self.is_valid_index(idx):
                            yield idx

    @property
    def ndim(self):
        return 2 if isinstance(self.universes[0][0], openmc.Universe) else 3

    @center.setter
    def center(self, center):
        cv.check_type('lattice center', center, Iterable, Real)
        cv.check_length('lattice center', center, 2, 3)
        self._center = center

    @Lattice.pitch.setter
    def pitch(self, pitch):
        cv.check_type('lattice pitch', pitch, Iterable, Real)
        cv.check_length('lattice pitch', pitch, 1, 2)
        for dim in pitch:
            cv.check_greater_than('lattice pitch', dim, 0)
        self._pitch = pitch

    @Lattice.universes.setter
    def universes(self, universes):
        cv.check_iterable_type('lattice universes', universes, openmc.Universe,
                               min_depth=2, max_depth=3)
        self._universes = universes

        # NOTE: This routine assumes that the user creates a "ragged" list of
        # lists, where each sub-list corresponds to one ring of Universes.
        # The sub-lists are ordered from outermost ring to innermost ring.
        # The Universes within each sub-list are ordered from the "top" in a
        # clockwise fashion.

        # Set the number of axial positions.
        if self.ndim == 3:
            self._num_axial = len(self._universes)
        else:
            self._num_axial = None

        # Set the number of rings and make sure this number is consistent for
        # all axial positions.
        if self.ndim == 3:
            self._num_rings = len(self._universes[0])
            for rings in self._universes:
                if len(rings) != self._num_rings:
                    msg = 'HexLattice ID={0:d} has an inconsistent number of ' \
                          'rings per axial positon'.format(self._id)
                    raise ValueError(msg)

        else:
            self._num_rings = len(self._universes)

        # Make sure there are the correct number of elements in each ring.
        if self.ndim == 3:
            for axial_slice in self._universes:
                # Check the center ring.
                if len(axial_slice[-1]) != 1:
                    msg = 'HexLattice ID={0:d} has the wrong number of ' \
                          'elements in the innermost ring.  Only 1 element is ' \
                          'allowed in the innermost ring.'.format(self._id)
                    raise ValueError(msg)

                # Check the outer rings.
                for r in range(self._num_rings-1):
                    if len(axial_slice[r]) != 6*(self._num_rings - 1 - r):
                        msg = 'HexLattice ID={0:d} has the wrong number of ' \
                              'elements in ring number {1:d} (counting from the '\
                              'outermost ring).  This ring should have {2:d} ' \
                              'elements.'.format(self._id, r,
                                                 6*(self._num_rings - 1 - r))
                        raise ValueError(msg)

        else:
            axial_slice = self._universes
            # Check the center ring.
            if len(axial_slice[-1]) != 1:
                msg = 'HexLattice ID={0:d} has the wrong number of ' \
                      'elements in the innermost ring.  Only 1 element is ' \
                      'allowed in the innermost ring.'.format(self._id)
                raise ValueError(msg)

            # Check the outer rings.
            for r in range(self._num_rings-1):
                if len(axial_slice[r]) != 6*(self._num_rings - 1 - r):
                    msg = 'HexLattice ID={0:d} has the wrong number of ' \
                          'elements in ring number {1:d} (counting from the '\
                          'outermost ring).  This ring should have {2:d} ' \
                          'elements.'.format(self._id, r,
                                             6*(self._num_rings - 1 - r))
                    raise ValueError(msg)

    def find_element(self, point):
        r"""Determine index of lattice element and local coordinates for a point

        Parameters
        ----------
        point : Iterable of float
            Cartesian coordinates of point

        Returns
        -------
        3-tuple of int
            Indices of corresponding lattice element in :math:`(x,\alpha,z)`
            bases
        numpy.ndarray
            Carestian coordinates of the point in the corresponding lattice
            element coordinate system

        """
        # Convert coordinates to skewed bases
        x = point[0] - self.center[0]
        y = point[1] - self.center[1]
        if self._num_axial is None:
            iz = 1
        else:
            z = point[2] - self.center[2]
            iz = floor(z/self.pitch[1] + 0.5*self.num_axial)
        alpha = y - x/sqrt(3.)
        ix = floor(x/(sqrt(0.75) * self.pitch[0]))
        ia = floor(alpha/self.pitch[0])

        # Check four lattice elements to see which one is closest based on local
        # coordinates
        d_min = np.inf
        for idx in [(ix, ia, iz), (ix + 1, ia, iz), (ix, ia + 1, iz),
                    (ix + 1, ia + 1, iz)]:
            p = self.get_local_coordinates(point, idx)
            d = p[0]**2 + p[1]**2
            if d < d_min:
                d_min = d
                idx_min = idx
                p_min = p

        return idx_min, p_min

    def get_local_coordinates(self, point, idx):
        r"""Determine local coordinates of a point within a lattice element

        Parameters
        ----------
        point : Iterable of float
            Cartesian coordinates of point
        idx : Iterable of int
            Indices of lattice element in :math:`(x,\alpha,z)` bases

        Returns
        -------
        3-tuple of float
            Cartesian coordinates of point in the lattice element coordinate
            system

        """
        x = point[0] - (self.center[0] + sqrt(0.75)*self.pitch[0]*idx[0])
        y = point[1] - (self.center[1] + (0.5*idx[0] + idx[1])*self.pitch[0])
        if self._num_axial is None:
            z = point[2]
        else:
            z = point[2] - (self.center[2] + (idx[2] + 0.5 - 0.5*self.num_axial)*
                            self.pitch[1])
        return (x, y, z)

    def get_universe_index(self, idx):
        r"""Return index in the universes array corresponding to a lattice element index

        Parameters
        ----------
        idx : Iterable of int
            Lattice element indices in the :math:`(x,\alpha,z)` coordinate
            system

        Returns
        -------
        2- or 3-tuple of int
            Indices used when setting the :attr:`HexLattice.universes` property

        """

        # First we determine which ring the index corresponds to.
        x = idx[0]
        a = idx[1]
        z = -a - x
        g = max(abs(x), abs(a), abs(z))

        # Next we use a clever method to figure out where along the ring we are.
        i_ring = self._num_rings - 1 - g
        if x >= 0:
            if a >= 0:
                i_within = x
            else:
                i_within = 2*g + z
        else:
            if a <= 0:
                i_within = 3*g - x
            else:
                i_within = 5*g - z

        if self.num_axial is None:
            return (i_ring, i_within)
        else:
            return (idx[2], i_ring, i_within)

    def is_valid_index(self, idx):
        r"""Determine whether lattice element index is within defined range

        Parameters
        ----------
        idx : Iterable of int
            Lattice element indices in the :math:`(x,\alpha,z)` coordinate
            system

        Returns
        -------
        bool
            Whether index is valid

        """
        x = idx[0]
        y = idx[1]
        z = 0 - y - x
        g = max(abs(x), abs(y), abs(z))
        if self.num_axial is None:
            return g < self.num_rings
        else:
            return g < self.num_rings and 0 <= idx[2] < self.num_axial

    def create_xml_subelement(self, xml_element):
        # Determine if XML element already contains subelement for this Lattice
        path = './hex_lattice[@id=\'{0}\']'.format(self._id)
        test = xml_element.find(path)

        # If the element does contain the Lattice subelement, then return
        if test is not None:
            return

        lattice_subelement = ET.Element("hex_lattice")
        lattice_subelement.set("id", str(self._id))

        if len(self._name) > 0:
            lattice_subelement.set("name", str(self._name))

        # Export the Lattice cell pitch
        pitch = ET.SubElement(lattice_subelement, "pitch")
        pitch.text = ' '.join(map(str, self._pitch))

        # Export the Lattice outer Universe (if specified)
        if self._outer is not None:
            outer = ET.SubElement(lattice_subelement, "outer")
            outer.text = '{0}'.format(self._outer._id)
            self._outer.create_xml_subelement(xml_element)

        lattice_subelement.set("n_rings", str(self._num_rings))

        if self._num_axial is not None:
            lattice_subelement.set("n_axial", str(self._num_axial))

        # Export Lattice cell center
        center = ET.SubElement(lattice_subelement, "center")
        center.text = ' '.join(map(str, self._center))

        # Export the Lattice nested Universe IDs.

        # 3D Lattices
        if self._num_axial is not None:
            slices = []
            for z in range(self._num_axial):
                # Initialize the center universe.
                universe = self._universes[z][-1][0]
                universe.create_xml_subelement(xml_element)

                # Initialize the remaining universes.
                for r in range(self._num_rings-1):
                    for theta in range(6*(self._num_rings - 1 - r)):
                        universe = self._universes[z][r][theta]
                        universe.create_xml_subelement(xml_element)

                # Get a string representation of the universe IDs.
                slices.append(self._repr_axial_slice(self._universes[z]))

            # Collapse the list of axial slices into a single string.
            universe_ids = '\n'.join(slices)

        # 2D Lattices
        else:
            # Initialize the center universe.
            universe = self._universes[-1][0]
            universe.create_xml_subelement(xml_element)

            # Initialize the remaining universes.
            for r in range(self._num_rings - 1):
                for theta in range(6*(self._num_rings - 1 - r)):
                    universe = self._universes[r][theta]
                    universe.create_xml_subelement(xml_element)

            # Get a string representation of the universe IDs.
            universe_ids = self._repr_axial_slice(self._universes)

        universes = ET.SubElement(lattice_subelement, "universes")
        universes.text = '\n' + universe_ids

        # Append the XML subelement for this Lattice to the XML element
        xml_element.append(lattice_subelement)

    def _repr_axial_slice(self, universes):
        """Return string representation for the given 2D group of universes.

        The 'universes' argument should be a list of lists of universes where
        each sub-list represents a single ring.  The first list should be the
        outer ring.
        """

        # Find the largest universe ID and count the number of digits so we can
        # properly pad the output string later.
        largest_id = max([max([univ._id for univ in ring])
                          for ring in universes])
        n_digits = len(str(largest_id))
        pad = ' '*n_digits
        id_form = '{: ^' + str(n_digits) + 'd}'

        # Initialize the list for each row.
        rows = [[] for i in range(1 + 4 * (self._num_rings-1))]
        middle = 2 * (self._num_rings - 1)

        # Start with the degenerate first ring.
        universe = universes[-1][0]
        rows[middle] = [id_form.format(universe._id)]

        # Add universes one ring at a time.
        for r in range(1, self._num_rings):
            # r_prime increments down while r increments up.
            r_prime = self._num_rings - 1 - r
            theta = 0
            y = middle + 2*r

            # Climb down the top-right.
            for i in range(r):
                # Add the universe.
                universe = universes[r_prime][theta]
                rows[y].append(id_form.format(universe._id))

                # Translate the indices.
                y -= 1
                theta += 1

            # Climb down the right.
            for i in range(r):
                # Add the universe.
                universe = universes[r_prime][theta]
                rows[y].append(id_form.format(universe._id))

                # Translate the indices.
                y -= 2
                theta += 1

            # Climb down the bottom-right.
            for i in range(r):
                # Add the universe.
                universe = universes[r_prime][theta]
                rows[y].append(id_form.format(universe._id))

                # Translate the indices.
                y -= 1
                theta += 1

            # Climb up the bottom-left.
            for i in range(r):
                # Add the universe.
                universe = universes[r_prime][theta]
                rows[y].insert(0, id_form.format(universe._id))

                # Translate the indices.
                y += 1
                theta += 1

            # Climb up the left.
            for i in range(r):
                # Add the universe.
                universe = universes[r_prime][theta]
                rows[y].insert(0, id_form.format(universe._id))

                # Translate the indices.
                y += 2
                theta += 1

            # Climb up the top-left.
            for i in range(r):
                # Add the universe.
                universe = universes[r_prime][theta]
                rows[y].insert(0, id_form.format(universe._id))

                # Translate the indices.
                y += 1
                theta += 1

        # Flip the rows and join each row into a single string.
        rows = [pad.join(x) for x in rows[::-1]]

        # Pad the beginning of the rows so they line up properly.
        for y in range(self._num_rings - 1):
            rows[y] = (self._num_rings - 1 - y)*pad + rows[y]
            rows[-1 - y] = (self._num_rings - 1 - y)*pad + rows[-1 - y]

        for y in range(self._num_rings % 2, self._num_rings, 2):
            rows[middle + y] = pad + rows[middle + y]
            if y != 0:
                rows[middle - y] = pad + rows[middle - y]

        # Join the rows together and return the string.
        universe_ids = '\n'.join(rows)
        return universe_ids

    @staticmethod
    def show_indices(num_rings):
        """Return a diagram of the hexagonal lattice layout with indices.

        This method can be used to show the proper indices to be used when
        setting the :attr:`HexLattice.universes` property. For example, running
        this method with num_rings=3 will return the following diagram::

                      (0, 0)
                (0,11)      (0, 1)
          (0,10)      (1, 0)      (0, 2)
                (1, 5)      (1, 1)
          (0, 9)      (2, 0)      (0, 3)
                (1, 4)      (1, 2)
          (0, 8)      (1, 3)      (0, 4)
                (0, 7)      (0, 5)
                      (0, 6)

        Parameters
        ----------
        num_rings : int
            Number of rings in the hexagonal lattice

        Returns
        -------
        str
            Diagram of the hexagonal lattice showing indices

        """

        # Find the largest string and count the number of digits so we can
        # properly pad the output string later
        largest_index = 6*(num_rings - 1)
        n_digits_index = len(str(largest_index))
        n_digits_ring = len(str(num_rings - 1))
        str_form = '({{:{}}},{{:{}}})'.format(n_digits_ring, n_digits_index)
        pad = ' '*(n_digits_index + n_digits_ring + 3)

        # Initialize the list for each row.
        rows = [[] for i in range(1 + 4 * (num_rings-1))]
        middle = 2 * (num_rings - 1)

        # Start with the degenerate first ring.
        rows[middle] = [str_form.format(num_rings - 1, 0)]

        # Add universes one ring at a time.
        for r in range(1, num_rings):
            # r_prime increments down while r increments up.
            r_prime = num_rings - 1 - r
            theta = 0
            y = middle + 2*r

            for i in range(r):
                # Climb down the top-right.
                rows[y].append(str_form.format(r_prime, theta))
                y -= 1
                theta += 1

            for i in range(r):
                # Climb down the right.
                rows[y].append(str_form.format(r_prime, theta))
                y -= 2
                theta += 1

            for i in range(r):
                # Climb down the bottom-right.
                rows[y].append(str_form.format(r_prime, theta))
                y -= 1
                theta += 1

            for i in range(r):
                # Climb up the bottom-left.
                rows[y].insert(0, str_form.format(r_prime, theta))
                y += 1
                theta += 1

            for i in range(r):
                # Climb up the left.
                rows[y].insert(0, str_form.format(r_prime, theta))
                y += 2
                theta += 1

            for i in range(r):
                # Climb up the top-left.
                rows[y].insert(0, str_form.format(r_prime, theta))
                y += 1
                theta += 1

        # Flip the rows and join each row into a single string.
        rows = [pad.join(x) for x in rows[::-1]]

        # Pad the beginning of the rows so they line up properly.
        for y in range(num_rings - 1):
            rows[y] = (num_rings - 1 - y)*pad + rows[y]
            rows[-1 - y] = (num_rings - 1 - y)*pad + rows[-1 - y]

        for y in range(num_rings % 2, num_rings, 2):
            rows[middle + y] = pad + rows[middle + y]
            if y != 0:
                rows[middle - y] = pad + rows[middle - y]

        # Join the rows together and return the string.
        return '\n'.join(rows)


def get_cylindrical_lattice_universe(pins, offsets, radii, univs):
    """Return a universe object that mimics a cylindrical lattice

    OpenMC does not have a cylindrical lattice object, so this function
    constructs a cylindrical lattice with a constant angular pitch by taking
    a making a base universe object and adding cells that are laid out in a
    cylindrical lattice. Each cell is then filled with a universe. The pins
    in each ring are laid out as follows:

                   (ring, pin)

                      (2, 0)
                (2,11)      (2, 1)
          (2,10)      (1, 0)      (2, 2)
                (1, 5)      (1, 1)
          (2, 9)      (0, 0)      (2, 3)
                (1, 4)      (1, 2)
          (2, 8)      (1, 3)      (2, 4)
                (2, 7)      (2, 5)
                      (2, 6)

    The following is an example of how to create a three ring cylindrical
    lattice:

    >>> # Instantiate some Materials and register the appropriate Nuclides
    >>> fuel = openmc.Material(material_id=1, name='fuel')
    >>> fuel.set_density('g/cc', 4.5)
    >>> fuel.add_nuclide('U235', 1.)

    >>> moderator = openmc.Material(material_id=2, name='moderator')
    >>> moderator.set_density('g/cc', 1.0)
    >>> moderator.add_element('H', 2.)
    >>> moderator.add_element('O', 1.)
    >>> moderator.add_s_alpha_beta('c_H_in_H2O')

    >>> fuel_cell = openmc.Cell(name='fuel')
    >>> mod_cell  = openmc.Cell(name='mod')
    >>> fuel_or = openmc.ZCylinder(R=0.3)
    >>> fuel_cell.region = -fuel_or
    >>> mod_cell.region  = +fuel_or

    >>> fuel_cell.fill = fuel
    >>> mod_cell.fill  = moderator

    >>> p = openmc.Universe(name='pin')
    >>> p.add_cells([fuel_cell, mod_cell])

    >>> pins     = [1  , 6  , 12]
    >>> offsets  = [0  , 0  , 15]
    >>> radii    = [0.0, 1.0, 2.0]
    >>> univs    = [[] for i in range(len(pins))]
    >>> univs[0] = [p] * pins[0]
    >>> univs[1] = [p] * pins[1]
    >>> univs[2] = [p] * pins[2]

    >>> lat_univ = openmc.get_cylindrical_lattice_universe(pins, offsets, radii, univs)

    Parameters
    ----------
    pins : Iterable of int
        Number of pins in each ring
    offsets : Iterable of float
        Angle offset (in degrees) of the first pin from the vertical.
    radii : Iterable of float
        The radii to the center of the cells in each of the rings.
    univs : Iterable of Iterable of openmc.Universe
        The universes to fill the cells of the cylindrical lattice.

    Returns
    -------
    openmc.Universe
        The Universe object that mimics a cylindrical lattice.

    """

    # Create lists to store the cells and surfaces
    cells = []
    cylinders = []
    planes = []

    # Create a universe to store all the cells that comprise the lattice
    lat_univ = openmc.Universe()

    # Create ring cylinders
    for r in range(len(pins)-1):
        cylinders.append(openmc.ZCylinder(R=(radii[r]+radii[r+1])/2.))

    # Create ring planes
    for r in range(len(pins)):
        planes.append([])
        if pins[r] > 1:
            for p in range(pins[r]):
                theta = (offsets[r] + (p-0.5)/float(pins[r])*360.)/180. * np.pi
                planes[-1].append(openmc.Plane(A=np.cos(theta), B=-np.sin(theta)))

    # Create ring cells
    for r in range(len(pins)):
        cells.append([])
        for p in range(pins[r]):
            cell = openmc.Cell()
            if r == 0:
                if len(pins) > 1:
                    cell.region = -cylinders[0]
            elif r == len(pins)-1:
                cell.region = +cylinders[r-1]
            else:
                cell.region = +cylinders[r-1] & -cylinders[r]

            if pins[r] > 1:
                if p == pins[r]-1:
                    cell.region = cell.region & +planes[r][p] & -planes[r][0]
                else:
                    cell.region = cell.region & +planes[r][p] & -planes[r][p+1]

            cells[-1].append(cell)

    # Fill ring cells with universes
    for r in range(len(pins)):
        for p in range(pins[r]):
            x = radii[r] * np.sin( (offsets[r] + p/float(pins[r])*360.)/180. * np.pi)
            y = radii[r] * np.cos( (offsets[r] + p/float(pins[r])*360.)/180. * np.pi)
            cells[r][p].fill = univs[r][p]
            cells[r][p].translation = [x,y,0.]
            lat_univ.add_cell(cells[r][p])

    return lat_univ
