import openmc
from universes import universes, cells

###############################################################################
#                     Create a dictionary of the assembly lattices
###############################################################################

c = universes['Core']
a = universes['Axial Blanket']
r = universes['Radial Blanket']
i = universes['Internal Blanket']
b = universes['Control Rod']
n = universes['Na Filled CRP']
s = universes['Radial Reflector']
x = universes['Axial Reflector']
m = universes['Empty Matrix']

# Instantiate the Lattices
lattices = {}
lattices['Internal Blanket Rodded'] = openmc.RectLattice(lattice_id=101, name='Internal Blanket Rodded')
lattices['Internal Blanket Rodded'].dimension = [32, 32]
lattices['Internal Blanket Rodded'].lower_left = [-80.0, -80.0]
lattices['Internal Blanket Rodded'].pitch = [5.0, 5.0]
lattices['Internal Blanket Rodded'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                                 [c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                                 [i, i, i, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                                 [i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                                 [i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m, m],
                                                 [i, i, i, i, i, i, i, i, i, i, c, b, b, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, b, b, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m],
                                                 [n, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                                 [n, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                                 [i, i, i, i, i, n, n, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s, s],
                                                 [i, i, i, i, i, n, n, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, n, n, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, n, n, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                 [b, i, i, i, i, i, i, n, n, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s]]

lattices['Internal Blanket Unrodded'] = openmc.RectLattice(lattice_id=102, name='Internal Blanket Unrodded')
lattices['Internal Blanket Unrodded'].dimension = [32, 32]
lattices['Internal Blanket Unrodded'].lower_left = [-80.0, -80.0]
lattices['Internal Blanket Unrodded'].pitch = [5.0, 5.0]
lattices['Internal Blanket Unrodded'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                                   [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                                   [c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                                   [c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                                   [c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                                   [c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                                   [c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                                   [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                                   [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                                   [c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                                   [i, i, i, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                                   [i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                                   [i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m, m],
                                                   [i, i, i, i, i, i, i, i, i, i, c, n, n, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m],
                                                   [i, i, i, i, i, i, i, i, i, i, i, n, n, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m],
                                                   [i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m],
                                                   [i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m],
                                                   [n, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                                   [n, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                                   [i, i, i, i, i, n, n, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s, s],
                                                   [i, i, i, i, i, n, n, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                                   [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, n, n, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                                   [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, n, n, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                   [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                   [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                   [n, i, i, i, i, i, i, n, n, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s]]

lattices['Internal Blanket Filled'] = openmc.RectLattice(lattice_id=103, name='Internal Blanket Filled')
lattices['Internal Blanket Filled'].dimension = [32, 32]
lattices['Internal Blanket Filled'].lower_left = [-80.0, -80.0]
lattices['Internal Blanket Filled'].pitch = [5.0, 5.0]
lattices['Internal Blanket Filled'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                                 [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                                 [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                                 [i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                                 [i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                                 [i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m, m],
                                                 [i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                                 [i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s]]

lattices['Core Rodded'] = openmc.RectLattice(lattice_id=104, name='Core Rodded')
lattices['Core Rodded'].dimension = [32, 32]
lattices['Core Rodded'].lower_left = [-80.0, -80.0]
lattices['Core Rodded'].pitch = [5.0, 5.0]
lattices['Core Rodded'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                     [c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                     [c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, b, b, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, b, b, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m],
                                     [n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                     [n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                     [c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s, s],
                                     [c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                     [b, c, c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s]]

lattices['Core Unrodded'] = openmc.RectLattice(lattice_id=105, name='Core Unrodded')
lattices['Core Unrodded'].dimension = [32, 32]
lattices['Core Unrodded'].lower_left = [-80.0, -80.0]
lattices['Core Unrodded'].pitch = [5.0, 5.0]
lattices['Core Unrodded'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                       [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                       [c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                       [c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                       [c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                       [c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, n, n, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m],
                                       [n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                       [n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                       [c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s, s],
                                       [c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                       [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                       [n, c, c, c, c, c, c, n, n, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s]]

lattices['Core Filled'] = openmc.RectLattice(lattice_id=106, name='Core Filled')
lattices['Core Filled'].dimension = [32, 32]
lattices['Core Filled'].lower_left = [-80.0, -80.0]
lattices['Core Filled'].pitch = [5.0, 5.0]
lattices['Core Filled'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                     [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, m],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s],
                                     [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, r, r, r, r, r, s, s, s]]

lattices['Axial Blanket Unrodded'] = openmc.RectLattice(lattice_id=107, name='Axial Blanket Unrodded')
lattices['Axial Blanket Unrodded'].dimension = [32, 32]
lattices['Axial Blanket Unrodded'].lower_left = [-80.0, -80.0]
lattices['Axial Blanket Unrodded'].pitch = [5.0, 5.0]
lattices['Axial Blanket Unrodded'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                                [a, a, a, a, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                                [a, a, a, a, a, a, a, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                                [a, a, a, n, n, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                                [a, a, a, n, n, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, m, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, n, n, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, n, n, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, m, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s, m],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, m],
                                                [n, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s],
                                                [n, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s],
                                                [a, a, a, a, a, n, n, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s, s],
                                                [a, a, a, a, a, n, n, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, n, n, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, n, n, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s],
                                                [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s],
                                                [n, a, a, a, a, a, a, n, n, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s]]

lattices['Axial Blanket Filled'] = openmc.RectLattice(lattice_id=108, name='Axial Blanket Filled')
lattices['Axial Blanket Filled'].dimension = [32, 32]
lattices['Axial Blanket Filled'].lower_left = [-80.0, -80.0]
lattices['Axial Blanket Filled'].pitch = [5.0, 5.0]
lattices['Axial Blanket Filled'].universes = [[s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [s, s, s, s, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [r, r, r, r, r, r, s, s, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m, m],
                                              [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m, m],
                                              [a, a, a, a, r, r, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, r, r, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, s, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, s, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, r, s, s, s, m, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, m, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, m, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, m],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, r, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s],
                                              [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, r, r, r, r, r, s, s, s]]

lattices['Axial Reflector Unrodded'] = openmc.RectLattice(lattice_id=109, name='Axial Reflector Unrodded')
lattices['Axial Reflector Unrodded'].dimension = [32, 32]
lattices['Axial Reflector Unrodded'].lower_left = [-80.0, -80.0]
lattices['Axial Reflector Unrodded'].pitch = [5.0, 5.0]
lattices['Axial Reflector Unrodded'].universes = [[x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m],
                                                  [x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m],
                                                  [x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m],
                                                  [n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                  [n, x, x, x, x, x, x, n, n, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x]]

lattices['Axial Reflector Filled'] = openmc.RectLattice(lattice_id=110, name='Axial Reflector Filled')
lattices['Axial Reflector Filled'].dimension = [32, 32]
lattices['Axial Reflector Filled'].lower_left = [-80.0, -80.0]
lattices['Axial Reflector Filled'].pitch = [5.0, 5.0]
lattices['Axial Reflector Filled'].universes = [[x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, m],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
                                                [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x]]


# Add assembly lattices to cells
cells['Internal Blanket Rodded'].fill   = lattices['Internal Blanket Rodded']
cells['Internal Blanket Unrodded'].fill = lattices['Internal Blanket Unrodded']
cells['Internal Blanket Filled'].fill   = lattices['Internal Blanket Filled']
cells['Core Rodded'].fill               = lattices['Core Rodded']
cells['Core Unrodded'].fill             = lattices['Core Unrodded']
cells['Core Filled'].fill               = lattices['Core Filled']
cells['Axial Blanket Unrodded'].fill    = lattices['Axial Blanket Unrodded']
cells['Axial Blanket Filled'].fill      = lattices['Axial Blanket Filled']
cells['Axial Reflector Unrodded'].fill  = lattices['Axial Reflector Unrodded']
cells['Axial Reflector Filled'].fill    = lattices['Axial Reflector Filled']
