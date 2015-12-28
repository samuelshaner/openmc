import openmc
import openmc.mgxs
import numpy as np
from materials import materials

###############################################################################
#                 Exporting to OpenMC geometry.xml File
###############################################################################

# Instantiate ZCylinder surfaces
fuel_cyl = openmc.ZCylinder(surface_id=1, x0=0, y0=0, R=0.54, name='Fuel OR')

# Instantiate Core boundaries
core_x_min = openmc.XPlane(surface_id=2, x0=-32.13, name='Core x-min')
core_y_min = openmc.YPlane(surface_id=3, y0=-32.13, name='Core y-min')
core_z_min = openmc.ZPlane(surface_id=4, z0= 0.0  , name='Core z-min')
core_x_max = openmc.XPlane(surface_id=5, x0= 32.13, name='Core x-max')
core_y_max = openmc.YPlane(surface_id=6, y0= 32.13, name='Core y-max')
core_z_max = openmc.ZPlane(surface_id=7, z0=214.20, name='Core z-max')

core_x_min.boundary_type = 'reflective'
core_y_min.boundary_type = 'vacuum'
core_z_min.boundary_type = 'reflective'
core_x_max.boundary_type = 'vacuum'
core_y_max.boundary_type = 'reflective'
core_z_max.boundary_type = 'vacuum'

# Instantiate Cells
cells = {}
cells['UO2']                       = openmc.Cell(cell_id=1, name='UO2 cell')
cells['MOX 4.3%']                  = openmc.Cell(cell_id=2, name='MOX 4.3 % cell')
cells['MOX 7.0%']                  = openmc.Cell(cell_id=3, name='MOX 7.0 % cell')
cells['MOX 8.7%']                  = openmc.Cell(cell_id=4, name='MOX 8.7 % cell')
cells['Fission Chamber']           = openmc.Cell(cell_id=5, name='fission chamber cell')
cells['Guide Tube']                = openmc.Cell(cell_id=6, name='guide tube cell')
cells['Reflector']                 = openmc.Cell(cell_id=7, name='reflector cell')
cells['Control Rod']               = openmc.Cell(cell_id=8, name='control rod cell')
cells['UO2 Moderator']             = openmc.Cell(cell_id=9, name='moderator cell')
cells['MOX 4.3% Moderator']        = openmc.Cell(cell_id=10, name='moderator cell')
cells['MOX 7.0% Moderator']        = openmc.Cell(cell_id=11, name='moderator cell')
cells['MOX 8.7% Moderator']        = openmc.Cell(cell_id=12, name='moderator cell')
cells['Fission Chamber Moderator'] = openmc.Cell(cell_id=13, name='moderator cell')
cells['Guide Tube Moderator']      = openmc.Cell(cell_id=14, name='moderator cell')
cells['Control Rod Moderator']     = openmc.Cell(cell_id=15, name='moderator cell')
cells['Core']                      = openmc.Cell(cell_id=16, name='core cell')
cells['UO2 Assembly']              = openmc.Cell(cell_id=17, name='UO2 assembly cell')
cells['MOX Assembly']              = openmc.Cell(cell_id=18, name='MOX assembly cell')
cells['Reflector Assembly']        = openmc.Cell(cell_id=19, name='Water assembly cell')

# Use surface half-spaces to define regions
cells['UO2'].region                       = -fuel_cyl
cells['MOX 4.3%'].region                  = -fuel_cyl
cells['MOX 7.0%'].region                  = -fuel_cyl
cells['MOX 8.7%'].region                  = -fuel_cyl
cells['Fission Chamber'].region           = -fuel_cyl
cells['Guide Tube'].region                = -fuel_cyl
cells['Control Rod'].region               = -fuel_cyl
cells['UO2 Moderator'].region             = +fuel_cyl
cells['MOX 4.3% Moderator'].region        = +fuel_cyl
cells['MOX 7.0% Moderator'].region        = +fuel_cyl
cells['MOX 8.7% Moderator'].region        = +fuel_cyl
cells['Fission Chamber Moderator'].region = +fuel_cyl
cells['Guide Tube Moderator'].region      = +fuel_cyl
cells['Control Rod Moderator'].region     = +fuel_cyl
cells['Core'].region                      = +core_x_min & +core_y_min & +core_z_min & -core_x_max & -core_y_max & -core_z_max

# Instantiate Universes
universes = {}
universes['Root']               = openmc.Universe(universe_id=0, name='root universe')
universes['UO2']                = openmc.Universe(universe_id=1, name='UO2 pin universe')
universes['MOX 4.3%']           = openmc.Universe(universe_id=2, name='MOX 4.3 % pin universe')
universes['MOX 7.0%']           = openmc.Universe(universe_id=3, name='MOX 7.0 % pin universe')
universes['MOX 8.7%']           = openmc.Universe(universe_id=4, name='MOX 8.7 % pin universe')
universes['Fission Chamber']    = openmc.Universe(universe_id=5, name='fission chamber universe')
universes['Guide Tube']         = openmc.Universe(universe_id=6, name='guide tube universe')
universes['Control Rod']        = openmc.Universe(universe_id=7, name='control rod universe')
universes['Reflector']          = openmc.Universe(universe_id=8, name='water universe')
universes['UO2 Assembly']       = openmc.Universe(universe_id=9, name='UO2 assembly universe')
universes['MOX Assembly']       = openmc.Universe(universe_id=10, name='MOX assembly universe')
universes['Reflector Assembly'] = openmc.Universe(universe_id=11, name='water assembly universe')

# Register Materials with Cells
cells['UO2'].fill                       = materials['UO2']
cells['MOX 4.3%'].fill                  = materials['MOX 4.3%']
cells['MOX 7.0%'].fill                  = materials['MOX 7.0%']
cells['MOX 8.7%'].fill                  = materials['MOX 8.7%']
cells['Fission Chamber'].fill           = materials['Fission Chamber']
cells['Guide Tube'].fill                = materials['Guide Tube']
cells['Control Rod'].fill               = materials['Control Rod']
cells['UO2 Moderator'].fill             = materials['Water']
cells['MOX 4.3% Moderator'].fill        = materials['Water']
cells['MOX 7.0% Moderator'].fill        = materials['Water']
cells['MOX 8.7% Moderator'].fill        = materials['Water']
cells['Fission Chamber Moderator'].fill = materials['Water']
cells['Guide Tube Moderator'].fill      = materials['Water']
cells['Control Rod Moderator'].fill     = materials['Water']
cells['Reflector'].fill                 = materials['Water']

# Register Cells with Universes
universes['Root'].add_cells([cells['Core']])
universes['UO2'].add_cells([cells['UO2'], cells['UO2 Moderator']])
universes['MOX 4.3%'].add_cells([cells['MOX 4.3%'], cells['MOX 4.3% Moderator']])
universes['MOX 7.0%'].add_cells([cells['MOX 7.0%'], cells['MOX 7.0% Moderator']])
universes['MOX 8.7%'].add_cells([cells['MOX 8.7%'], cells['MOX 8.7% Moderator']])
universes['Fission Chamber'].add_cells([cells['Fission Chamber'], cells['Fission Chamber Moderator']])
universes['Guide Tube'].add_cells([cells['Guide Tube'], cells['Guide Tube Moderator']])
universes['Control Rod'].add_cells([cells['Control Rod'], cells['Control Rod Moderator']])
universes['Reflector'].add_cells([cells['Reflector']])
universes['UO2 Assembly'].add_cells([cells['UO2 Assembly']])
universes['MOX Assembly'].add_cells([cells['MOX Assembly']])
universes['Reflector Assembly'].add_cells([cells['Reflector Assembly']])

# Instantiate the Lattices
lattices = {}
lattices['UO2 Assembly'] = openmc.RectLattice(lattice_id=101, name='17x17 UO2 assembly')
lattices['UO2 Assembly'].dimension = [17, 17]
lattices['UO2 Assembly'].lower_left = [-10.71, -10.71]
lattices['UO2 Assembly'].pitch = [1.26, 1.26]
u = universes['UO2']
g = universes['Guide Tube']
f = universes['Fission Chamber']
lattices['UO2 Assembly'].universes = [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, u, u, u, g, u, u, g, u, u, g, u, u, u, u, u],
                                      [u, u, u, g, u, u, u, u, u, u, u, u, u, g, u, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, g, u, u, g, u, u, g, u, u, g, u, u, g, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, g, u, u, g, u, u, f, u, u, g, u, u, g, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, g, u, u, g, u, u, g, u, u, g, u, u, g, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, u, g, u, u, u, u, u, u, u, u, u, g, u, u, u],
                                      [u, u, u, u, u, g, u, u, g, u, u, g, u, u, u, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                      [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]

cells['UO2 Assembly'].fill = lattices['UO2 Assembly']

lattices['MOX Assembly'] = openmc.RectLattice(lattice_id=102, name='17x17 MOX assembly')
lattices['MOX Assembly'].dimension = [17, 17]
lattices['MOX Assembly'].lower_left = [-10.71, -10.71]
lattices['MOX Assembly'].pitch = [1.26, 1.26]
m = universes['MOX 4.3%']
n = universes['MOX 7.0%']
o = universes['MOX 8.7%']
g = universes['Guide Tube']
f = universes['Fission Chamber']
lattices['MOX Assembly'].universes = [[m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                      [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
                                      [m, n, n, n, n, g, n, n, g, n, n, g, n, n, n, n, m],
                                      [m, n, n, g, n, o, o, o, o, o, o, o, n, g, n, n, m],
                                      [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
                                      [m, n, g, o, o, g, o, o, g, o, o, g, o, o, g, n, m],
                                      [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                      [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                      [m, n, g, o, o, g, o, o, f, o, o, g, o, o, g, n, m],
                                      [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                      [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                      [m, n, g, o, o, g, o, o, g, o, o, g, o, o, g, n, m],
                                      [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
                                      [m, n, n, g, n, o, o, o, o, o, o, o, n, g, n, n, m],
                                      [m, n, n, n, n, g, n, n, g, n, n, g, n, n, n, n, m],
                                      [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
                                      [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]]

cells['MOX Assembly'].fill = lattices['MOX Assembly']

lattices['Reflector Assembly'] = openmc.RectLattice(lattice_id=103, name='1x1 water assembly')
lattices['Reflector Assembly'].dimension = [1,1]
lattices['Reflector Assembly'].lower_left = [-10.71, -10.71]
lattices['Reflector Assembly'].pitch = [21.42, 21.42]
w = universes['Reflector']
lattices['Reflector Assembly'].universes = [[w]]
cells['Reflector Assembly'].fill = lattices['Reflector Assembly']

lattices['Core'] = openmc.RectLattice(lattice_id=104, name='3x3 core lattice')
lattices['Core'].dimension = [3,3,10]
lattices['Core'].lower_left = [-32.13, -32.13, 0.0]
lattices['Core'].pitch = [21.42, 21.42, 21.42]
w = universes['Reflector Assembly']
u = universes['UO2 Assembly']
m = universes['MOX Assembly']
lattices['Core'].universes = [[[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[u, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[w, w, w],
                               [w, w, w],
                               [w, w, w]]]

cells['Core'].fill = lattices['Core']

# Instantiate a Geometry and register the root Universe
geometry = openmc.Geometry()
geometry.root_universe = universes['Root']

# Instantiate a GeometryFile, register Geometry, and export to XML
geometry_file = openmc.GeometryFile()
geometry_file.geometry = geometry
geometry_file.export_to_xml()
