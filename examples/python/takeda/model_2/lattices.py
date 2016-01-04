import openmc
from universes import universes, cells

###############################################################################
#                     Create a dictionary of the assembly lattices
###############################################################################

# Instantiate the Lattices
lattices = {}
lattices['Blanket Upper'] = openmc.RectLattice(lattice_id=101, name='Blanket Upper')
lattices['Blanket Upper'].dimension = [14, 14]
lattices['Blanket Upper'].lower_left = [-35.0, -35.0]
lattices['Blanket Upper'].pitch = [5.0, 5.0]
a = universes['Axial Blanket']
r = universes['Radial Blanket']
c = universes['Control Rod']
lattices['Blanket Upper'].universes = [[r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                                       [a, a, a, r, r, r, r, r, r, r, r, r, r, r],
                                       [a, a, a, a, a, a, r, r, r, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, r, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, a, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, a, r, r, r],
                                       [a, a, a, a, a, a, a, c, c, a, a, r, r, r]]

lattices['Blanket Lower'] = openmc.RectLattice(lattice_id=102, name='Blanket Lower')
lattices['Blanket Lower'].dimension = [14, 14]
lattices['Blanket Lower'].lower_left = [-35.0, -35.0]
lattices['Blanket Lower'].pitch = [5.0, 5.0]
a = universes['Axial Blanket']
r = universes['Radial Blanket']
n = universes['Na Filled CRP']
lattices['Blanket Lower'].universes = [[r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                                       [a, a, a, r, r, r, r, r, r, r, r, r, r, r],
                                       [a, a, a, a, a, a, r, r, r, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, r, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, r, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, r, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, a, r, r, r],
                                       [a, a, a, a, a, a, a, a, a, a, a, r, r, r],
                                       [a, a, a, a, a, a, a, n, n, a, a, r, r, r]]

lattices['Core Upper'] = openmc.RectLattice(lattice_id=103, name='Core Upper')
lattices['Core Upper'].dimension = [14, 14]
lattices['Core Upper'].lower_left = [-35.0, -35.0]
lattices['Core Upper'].pitch = [5.0, 5.0]
c = universes['Core']
b = universes['Radial Blanket']
r = universes['Control Rod']
lattices['Core Upper'].universes = [[b, b, b, b, b, b, b, b, b, b, b, b, b, b],
                                    [b, b, b, b, b, b, b, b, b, b, b, b, b, b],
                                    [b, b, b, b, b, b, b, b, b, b, b, b, b, b],
                                    [c, c, c, b, b, b, b, b, b, b, b, b, b, b],
                                    [c, c, c, c, c, c, b, b, b, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, b, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, c, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, c, b, b, b],
                                    [c, c, c, c, c, c, c, r, r, c, c, b, b, b]]

lattices['Core Lower'] = openmc.RectLattice(lattice_id=104, name='Core Lower')
lattices['Core Lower'].dimension = [14, 14]
lattices['Core Lower'].lower_left = [-35.0, -35.0]
lattices['Core Lower'].pitch = [5.0, 5.0]
c = universes['Core']
b = universes['Radial Blanket']
n = universes['Na Filled CRP']
lattices['Core Lower'].universes = [[b, b, b, b, b, b, b, b, b, b, b, b, b, b],
                                    [b, b, b, b, b, b, b, b, b, b, b, b, b, b],
                                    [b, b, b, b, b, b, b, b, b, b, b, b, b, b],
                                    [c, c, c, b, b, b, b, b, b, b, b, b, b, b],
                                    [c, c, c, c, c, c, b, b, b, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, b, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, b, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, b, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, c, b, b, b],
                                    [c, c, c, c, c, c, c, c, c, c, c, b, b, b],
                                    [c, c, c, c, c, c, c, n, n, c, c, b, b, b]]

# Add assembly lattices to cells
cells['Blanket Upper'].fill = lattices['Blanket Upper']
cells['Blanket Lower'].fill = lattices['Blanket Lower']
cells['Core Upper'].fill    = lattices['Core Upper']
cells['Core Lower'].fill    = lattices['Core Lower']
