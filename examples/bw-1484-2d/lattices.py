import openmc
import openmc.mgxs
import numpy as np
from universes import universes, cells

###############################################################################
#                     Create a dictionary of the assembly lattices
###############################################################################

# Instantiate the Lattices
lattices = {}
lattices['Core 1 Lattice']  = openmc.RectLattice(lattice_id=101, name='Core 1 Lattice')
lattices['Core 2 Lattice']  = openmc.RectLattice(lattice_id=102, name='Core 2 Lattice')
lattices['Core 3 Lattice']  = openmc.RectLattice(lattice_id=103, name='Core 3 Lattice')
lattices['Core 4 Lattice']  = openmc.RectLattice(lattice_id=104, name='Core 4 Lattice')
lattices['Core 5 Lattice']  = openmc.RectLattice(lattice_id=105, name='Core 5 Lattice')
lattices['Core 6 Lattice']  = openmc.RectLattice(lattice_id=106, name='Core 6 Lattice')
lattices['Core 7 Lattice']  = openmc.RectLattice(lattice_id=107, name='Core 7 Lattice')
lattices['Core 8 Lattice']  = openmc.RectLattice(lattice_id=108, name='Core 8 Lattice')
lattices['Core 9 Lattice']  = openmc.RectLattice(lattice_id=109, name='Core 9 Lattice')
lattices['Core 10 Lattice'] = openmc.RectLattice(lattice_id=110, name='Core 10 Lattice')
lattices['Core 11 Lattice'] = openmc.RectLattice(lattice_id=111, name='Core 11 Lattice')
lattices['Core 12 Lattice'] = openmc.RectLattice(lattice_id=112, name='Core 12 Lattice')
lattices['Core 13 Lattice'] = openmc.RectLattice(lattice_id=113, name='Core 13 Lattice')
lattices['Core 14 Lattice'] = openmc.RectLattice(lattice_id=114, name='Core 14 Lattice')
lattices['Core 15 Lattice'] = openmc.RectLattice(lattice_id=115, name='Core 15 Lattice')
lattices['Core 16 Lattice'] = openmc.RectLattice(lattice_id=116, name='Core 16 Lattice')
lattices['Core 17 Lattice'] = openmc.RectLattice(lattice_id=117, name='Core 17 Lattice')
lattices['Core 18 Lattice'] = openmc.RectLattice(lattice_id=118, name='Core 18 Lattice')
lattices['Core 19 Lattice'] = openmc.RectLattice(lattice_id=119, name='Core 19 Lattice')
lattices['Core 20 Lattice'] = openmc.RectLattice(lattice_id=120, name='Core 20 Lattice')
lattices['Core 21 Lattice'] = openmc.RectLattice(lattice_id=121, name='Core 21 Lattice')

lattices['Core 1 Lattice'].dimension  = [78, 78]
lattices['Core 2 Lattice'].dimension  = [78, 78]
lattices['Core 3 Lattice'].dimension  = [78, 78]
lattices['Core 4 Lattice'].dimension  = [78, 78]
lattices['Core 5 Lattice'].dimension  = [78, 78]
lattices['Core 6 Lattice'].dimension  = [78, 78]
lattices['Core 7 Lattice'].dimension  = [78, 78]
lattices['Core 8 Lattice'].dimension  = [78, 78]
lattices['Core 9 Lattice'].dimension  = [78, 78]
lattices['Core 10 Lattice'].dimension = [78, 78]
lattices['Core 11 Lattice'].dimension = [78, 78]
lattices['Core 12 Lattice'].dimension = [78, 78]
lattices['Core 13 Lattice'].dimension = [78, 78]
lattices['Core 14 Lattice'].dimension = [78, 78]
lattices['Core 15 Lattice'].dimension = [78, 78]
lattices['Core 16 Lattice'].dimension = [78, 78]
lattices['Core 17 Lattice'].dimension = [78, 78]
lattices['Core 18 Lattice'].dimension = [78, 78]
lattices['Core 19 Lattice'].dimension = [78, 78]
lattices['Core 20 Lattice'].dimension = [78, 78]
lattices['Core 21 Lattice'].dimension = [78, 78]

lattices['Core 1 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 2 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 3 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 4 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 5 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 6 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 7 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 8 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 9 Lattice'].lower_left  = [-39*1.636, -39*1.636]
lattices['Core 10 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 11 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 12 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 13 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 14 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 15 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 16 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 17 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 18 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 19 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 20 Lattice'].lower_left = [-39*1.636, -39*1.636]
lattices['Core 21 Lattice'].lower_left = [-39*1.636, -39*1.636]

lattices['Core 1 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 2 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 3 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 4 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 5 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 6 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 7 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 8 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 9 Lattice'].pitch  = [1.636, 1.636]
lattices['Core 10 Lattice'].pitch = [1.636, 1.636]
lattices['Core 11 Lattice'].pitch = [1.636, 1.636]
lattices['Core 12 Lattice'].pitch = [1.636, 1.636]
lattices['Core 13 Lattice'].pitch = [1.636, 1.636]
lattices['Core 14 Lattice'].pitch = [1.636, 1.636]
lattices['Core 15 Lattice'].pitch = [1.636, 1.636]
lattices['Core 16 Lattice'].pitch = [1.636, 1.636]
lattices['Core 17 Lattice'].pitch = [1.636, 1.636]
lattices['Core 18 Lattice'].pitch = [1.636, 1.636]
lattices['Core 19 Lattice'].pitch = [1.636, 1.636]
lattices['Core 20 Lattice'].pitch = [1.636, 1.636]
lattices['Core 21 Lattice'].pitch = [1.636, 1.636]

f = universes['Fuel Rod Core 1']
a = universes['Al Rod Core 1']
b = universes['B4C Rod Core 1']
r = universes['Reflector Core 1']

lattices['Core 1 Lattice'].universes = [[r] * 78] * 27 + \
                                       [[r] * 36 + [f] * 6  + [r] * 36] + \
                                       [[r] * 34 + [f] * 10 + [r] * 34] + \
                                       [[r] * 32 + [f] * 14 + [r] * 32] + \
                                       [[r] * 31 + [f] * 16 + [r] * 31] + \
                                       [[r] * 30 + [f] * 18 + [r] * 30] + \
                                       [[r] * 29 + [f] * 20 + [r] * 29] * 2 + \
                                       [[r] * 28 + [f] * 22 + [r] * 28] * 2 + \
                                       [[r] * 27 + [f] * 24 + [r] * 27] * 6 + \
                                       [[r] * 28 + [f] * 22 + [r] * 28] * 2 + \
                                       [[r] * 29 + [f] * 20 + [r] * 29] * 2 + \
                                       [[r] * 30 + [f] * 18 + [r] * 30] + \
                                       [[r] * 31 + [f] * 16 + [r] * 31] + \
                                       [[r] * 32 + [f] * 14 + [r] * 32] + \
                                       [[r] * 34 + [f] * 10 + [r] * 34] + \
                                       [[r] * 36 + [f] * 6  + [r] * 36] + \
                                       [[r] * 78] * 27

f = universes['Fuel Rod Core 2']
a = universes['Al Rod Core 2']
b = universes['B4C Rod Core 2']
r = universes['Reflector Core 2']

lattices['Core 2 Lattice'].universes = [[r] * 78] * 18 + \
                                       [[r] * 18 + [f] * 42 + [r] * 18] * 42 + \
                                       [[r] * 78] * 18

f = universes['Fuel Rod Core 3']
a = universes['Al Rod Core 3']
b = universes['B4C Rod Core 3']
r = universes['Reflector Core 3']

lattices['Core 3 Lattice'].universes = [[r] * 78] * 17 + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] * 14 + \
                                       [[r] * 78] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] * 14 + \
                                       [[r] * 78] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] * 14 + \
                                       [[r] * 78] * 17

f = universes['Fuel Rod Core 4']
a = universes['Al Rod Core 4']
b = universes['B4C Rod Core 4']
r = universes['Reflector Core 4']

lattices['Core 4 Lattice'].universes = [[r] * 78] * 17 + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 19 + [b,r] * 13 + [b] * 3 + [r,b] * 6 + [r] * 18] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 19 + [b,r] * 13 + [b] * 3 + [r,b] * 6 + [r] * 18] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [r] + [f] * 14 + [r] + [f] * 14 + [r] * 17] + \
                                       [[r] * 17 + [f] * 14 + [b] + [f] * 14 + [b] + [f] * 14 + [r] * 17] + \
                                       [[r] * 78] * 17

f = universes['Fuel Rod Core 5']
a = universes['Al Rod Core 5']
b = universes['B4C Rod Core 5']
r = universes['Reflector Core 5']

lattices['Core 5 Lattice'].universes = [[r] * 78] * 16 + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 78] + \
                                       [[r] * 17 + [b,r,b,r,r,b,r,b,r,r,b,r,b,r,b] + [r,r,b] * 5 + [r,b,r,b,r,r,b,r,b,r,r,b,r,b] + [r] * 17] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 17 + [b,r,b,r,r,b,r,b,r,r,b,r,b,r,b] + [r,r,b] * 5 + [r,b,r,b,r,r,b,r,b,r,r,b,r,b] + [r] * 17] + \
                                       [[r] * 78] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 78] * 16

f = universes['Fuel Rod Core 6']
a = universes['Al Rod Core 6']
b = universes['B4C Rod Core 6']
r = universes['Reflector Core 6']

lattices['Core 6 Lattice'].universes = [[r] * 78] * 16 + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,b] + [f] * 14 + [b,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 17 + [b,r,b,r,r,b,r,b,r,r,b,r,b,r,b] + [r,r,b] * 5 + [r,b,r,b,r,r,b,r,b,r,r,b,r,b] + [r] * 17] + \
                                       [[r] * 78] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 78] + \
                                       [[r] * 17 + [b,r,b,r,r,b,r,b,r,r,b,r,b,r,b] + [r,r,b] * 5 + [r,b,r,b,r,r,b,r,b,r,r,b,r,b] + [r] * 17] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [b,r] + [f] * 14 + [r,b] + [f] * 14 + [r] * 16] + \
                                       [[r] * 16 + [f] * 14 + [r,r] + [f] * 14 + [r,r] + [f] * 14 + [r] * 16] + \
                                       [[r] * 78] * 16

f = universes['Fuel Rod Core 7']
a = universes['Al Rod Core 7']
b = universes['B4C Rod Core 7']
r = universes['Reflector Core 7']

lattices['Core 7 Lattice'].universes = [[r] * 78] * 15 + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 78] * 2 + \
                                       [[r] * 15 + [r,r,r,b] * 3 + [r] * 7 + [b] + [r] * 8 + [b] + [r] * 7 + [b,r,r,r] * 3 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [r,r,r,b] * 3 + [r] * 7 + [b] + [r] * 8 + [b] + [r] * 7 + [b,r,r,r] * 3 + [r] * 15] + \
                                       [[r] * 78] * 2 + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,b] + [f] * 14 + [b,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 78] * 15

f = universes['Fuel Rod Core 8']
a = universes['Al Rod Core 8']
b = universes['B4C Rod Core 8']
r = universes['Reflector Core 8']

lattices['Core 8 Lattice'].universes = [[r] * 78] * 15 + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 78] + \
                                       [[r] * 15 + [r,r,r,b] * 3 + [r] * 7 + [b] + [r] * 8 + [b] + [r] * 7 + [b,r,r,r] * 3 + [r] * 15] + \
                                       [[r] * 78] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 78] + \
                                       [[r] * 15 + [r,r,r,b] * 3 + [r] * 7 + [b] + [r] * 8 + [b] + [r] * 7 + [b,r,r,r] * 3 + [r] * 15] + \
                                       [[r] * 78] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,b,r] + [f] * 14 + [r,b,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 15 + [f] * 14 + [r,r,r] + [f] * 14 + [r,r,r] + [f] * 14 + [r] * 15] + \
                                       [[r] * 78] * 15

f = universes['Fuel Rod Core 9']
a = universes['Al Rod Core 9']
b = universes['B4C Rod Core 9']
r = universes['Reflector Core 9']

lattices['Core 9 Lattice'].universes = [[r] * 78] * 14 + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 78] * 4 + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 78] * 4 + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 14 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 4 + [f] * 14 + [r] * 14] + \
                                       [[r] * 78] * 14

f = universes['Fuel Rod Core 10']
a = universes['Al Rod Core 10']
b = universes['B4C Rod Core 10']
r = universes['Reflector Core 10']

lattices['Core 10 Lattice'].universes = [[r] * 78] * 15 + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 78] * 3 + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 78] * 3 + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 3 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 3 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 78] * 15

f = universes['Fuel Rod Core 11']
a = universes['Al Rod Core 11']
b = universes['B4C Rod Core 11']
r = universes['Reflector Core 11']
x = universes['SS Sheet Cross Core 11']
h = universes['SS Sheet Horiz Core 11']
v = universes['SS Sheet Verti Core 11']

lattices['Core 11 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 78] * 10

f = universes['Fuel Rod Core 12']
a = universes['Al Rod Core 12']
b = universes['B4C Rod Core 12']
r = universes['Reflector Core 12']
x = universes['SS Sheet Cross Core 12']
h = universes['SS Sheet Horiz Core 12']
v = universes['SS Sheet Verti Core 12']

lattices['Core 12 Lattice'].universes = [[r] * 78] * 11 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 78] * 11

f = universes['Fuel Rod Core 13']
a = universes['Al Rod Core 13']
b = universes['B4C Rod Core 13']
r = universes['Reflector Core 13']
x = universes['BAl Sheet Cross Core 13']
h = universes['BAl Sheet Horiz Core 13']
v = universes['BAl Sheet Verti Core 13']

lattices['Core 13 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 78] * 10

f = universes['Fuel Rod Core 14']
a = universes['Al Rod Core 14']
b = universes['B4C Rod Core 14']
r = universes['Reflector Core 14']
x = universes['BAl Sheet Cross Core 14']
h = universes['BAl Sheet Horiz Core 14']
v = universes['BAl Sheet Verti Core 14']

lattices['Core 14 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 78] * 10

f = universes['Fuel Rod Core 15']
a = universes['Al Rod Core 15']
b = universes['B4C Rod Core 15']
r = universes['Reflector Core 15']
x = universes['BAl Sheet Cross Core 15']
h = universes['BAl Sheet Horiz Core 15']
v = universes['BAl Sheet Verti Core 15']

lattices['Core 15 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 78] * 10

f = universes['Fuel Rod Core 16']
a = universes['Al Rod Core 16']
b = universes['B4C Rod Core 16']
r = universes['Reflector Core 16']
x = universes['BAl Sheet Cross Core 16']
h = universes['BAl Sheet Horiz Core 16']
v = universes['BAl Sheet Verti Core 16']

lattices['Core 16 Lattice'].universes = [[r] * 78] * 11 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 78] * 11

f = universes['Fuel Rod Core 17']
a = universes['Al Rod Core 17']
b = universes['B4C Rod Core 17']
r = universes['Reflector Core 17']
x = universes['BAl Sheet Cross Core 17']
h = universes['BAl Sheet Horiz Core 17']
v = universes['BAl Sheet Verti Core 17']

lattices['Core 17 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 78] * 10

f = universes['Fuel Rod Core 18']
a = universes['Al Rod Core 18']
b = universes['B4C Rod Core 18']
r = universes['Reflector Core 18']
x = universes['BAl Sheet Cross Core 18']
h = universes['BAl Sheet Horiz Core 18']
v = universes['BAl Sheet Verti Core 18']

lattices['Core 18 Lattice'].universes = [[r] * 78] * 11 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 78] * 11

f = universes['Fuel Rod Core 19']
a = universes['Al Rod Core 19']
b = universes['B4C Rod Core 19']
r = universes['Reflector Core 19']
x = universes['BAl Sheet Cross Core 19']
h = universes['BAl Sheet Horiz Core 19']
v = universes['BAl Sheet Verti Core 19']

lattices['Core 19 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [f] * 14 + [v] + [f] * 14 + [v] + [f] * 14 + [r] * 17] + \
                                        [[r] * 17 + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [v] + [a] + [f] * 12 + [a] + [r] * 17] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 7 + \
                                        [[r] * 78] * 10

f = universes['Fuel Rod Core 20']
a = universes['Al Rod Core 20']
b = universes['B4C Rod Core 20']
r = universes['Reflector Core 20']
x = universes['BAl Sheet Cross Core 20']
h = universes['BAl Sheet Horiz Core 20']
v = universes['BAl Sheet Verti Core 20']

lattices['Core 20 Lattice'].universes = [[r] * 78] * 11 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [f] * 14 + [r, v] + [f] * 14 + [v, r] + [f] * 14 + [r] * 16] + \
                                        [[r] * 16 + [a] + [f] * 12 + [a, r, v, a] + [f] * 12 + [a, v, r, a] + [f] * 12 + [a] + [r] * 16] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 78] * 11

f = universes['Fuel Rod Core 21']
a = universes['Al Rod Core 21']
b = universes['B4C Rod Core 21']
r = universes['Reflector Core 21']
x = universes['BAl Sheet Cross Core 21']
h = universes['BAl Sheet Horiz Core 21']
v = universes['BAl Sheet Verti Core 21']

lattices['Core 21 Lattice'].universes = [[r] * 78] * 10 + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 2 + [v] + [a] + [f] * 12 + [a] + [v] + [r] * 2 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 2 + [v] + [a] + [f] * 12 + [a] + [v] + [r] * 2 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 2 + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 2 + [v] + [a] + [f] * 12 + [a] + [v] + [r] * 2 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 2 + [v] + [a] + [f] * 12 + [a] + [v] + [r] * 2 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 10 + [h] * 21 + [x] + [h] * 14 + [x] + [h] * 21 + [r] * 10] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 2 + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 2 + [v] + [a] + [f] * 12 + [a] + [v] + [r] * 2 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [f] * 14 + [r] * 2 + [v] + [f] * 14 + [v] + [r] * 2 + [f] * 14 + [r] * 15] + \
                                        [[r] * 15 + [a] + [f] * 12 + [a] + [r] * 2 + [v] + [a] + [f] * 12 + [a] + [v] + [r] * 2 + [a] + [f] * 12 + [a] + [r] * 15] + \
                                        [[r] * 31 + [v] + [r] * 14 + [v] + [r] * 31] * 5 + \
                                        [[r] * 78] * 10


# Add lattice to cells
cells['Core 1'].fill       = lattices['Core 1 Lattice']
cells['Core 2'].fill       = lattices['Core 2 Lattice']
cells['Core 3'].fill       = lattices['Core 3 Lattice']
cells['Core 3'].fill       = lattices['Core 4 Lattice']
cells['Core 5'].fill       = lattices['Core 5 Lattice']
cells['Core 6'].fill       = lattices['Core 6 Lattice']
cells['Core 7'].fill       = lattices['Core 7 Lattice']
cells['Core 8'].fill       = lattices['Core 8 Lattice']
cells['Core 9'].fill       = lattices['Core 9 Lattice']
cells['Core 10'].fill      = lattices['Core 10 Lattice']
cells['Core 11'].fill      = lattices['Core 11 Lattice']
cells['Core 12'].fill      = lattices['Core 12 Lattice']
cells['Core 13'].fill      = lattices['Core 13 Lattice']
cells['Core 14'].fill      = lattices['Core 14 Lattice']
cells['Core 15'].fill      = lattices['Core 15 Lattice']
cells['Core 16'].fill      = lattices['Core 16 Lattice']
cells['Core 17'].fill      = lattices['Core 17 Lattice']
cells['Core 18'].fill      = lattices['Core 18 Lattice']
cells['Core 19'].fill      = lattices['Core 19 Lattice']
cells['Core 20'].fill      = lattices['Core 20 Lattice']
cells['Core 21'].fill      = lattices['Core 21 Lattice']
