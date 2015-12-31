import openmc
from lattices import lattices, universes, cells

###############################################################################
#                      Simulation Input File Parameters
###############################################################################

# OpenMC simulation parameters
batches = 200
inactive = 100
particles = 10000


###############################################################################
#                 Exporting to OpenMC materials.xml File
###############################################################################

from materials import materials

# Instantiate a MaterialsFile, register all Materials, and export to XML
materials_file = openmc.MaterialsFile()
materials_file.default_xs = '300k'
materials_file.add_materials(materials.values())
materials_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC geometry.xml File
###############################################################################

# Instantiate Core boundaries
core_x_min = openmc.XPlane(surface_id=2, x0=-32.13, name='Core x-min')
core_y_min = openmc.YPlane(surface_id=3, y0=-32.13, name='Core y-min')
core_z_min = openmc.ZPlane(surface_id=4, z0=-32.13, name='Core z-min')
core_x_max = openmc.XPlane(surface_id=5, x0= 32.13, name='Core x-max')
core_y_max = openmc.YPlane(surface_id=6, y0= 32.13, name='Core y-max')
core_z_max = openmc.ZPlane(surface_id=7, z0= 32.13, name='Core z-max')

core_x_min.boundary_type = 'reflective'
core_y_min.boundary_type = 'vacuum'
core_z_min.boundary_type = 'reflective'
core_x_max.boundary_type = 'vacuum'
core_y_max.boundary_type = 'reflective'
core_z_max.boundary_type = 'vacuum'

cells['Core'].region = +core_x_min & +core_y_min & +core_z_min & -core_x_max & -core_y_max & -core_z_max

lattices['Core'] = openmc.RectLattice(lattice_id=201, name='3x3 core lattice')
lattices['Core'].dimension = [3,3,9]
lattices['Core'].lower_left = [-32.13, -32.13, -32.13]
lattices['Core'].pitch = [21.42, 21.42, 7.14]
w = universes['Reflector Unrodded Assembly']
x = universes['Reflector Rodded Assembly']
u = universes['UO2 Unrodded Assembly']
v = universes['UO2 Rodded Assembly']
m = universes['MOX Unrodded Assembly']
n = universes['MOX Rodded Assembly']
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
                              [[v, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[v, m, w],
                               [m, u, w],
                               [w, w, w]],
                              [[x, x, w],
                               [x, x, w],
                               [w, w, w]],
                              [[x, x, w],
                               [x, x, w],
                               [w, w, w]],
                              [[x, x, w],
                               [x, x, w],
                               [w, w, w]]]

# Add Core lattice to Core cell
cells['Core'].fill = lattices['Core']

# Instantiate a Geometry and register the root Universe
geometry = openmc.Geometry()
geometry.root_universe = universes['Root']

# Instantiate a GeometryFile, register Geometry, and export to XML
geometry_file = openmc.GeometryFile()
geometry_file.geometry = geometry
geometry_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC settings.xml File
###############################################################################

# Instantiate a SettingsFile, set all runtime parameters, and export to XML
settings_file = openmc.SettingsFile()
settings_file.energy_mode = "multi-group"
settings_file.cross_sections = "./mg_cross_sections.xml"
settings_file.batches = batches
settings_file.inactive = inactive
settings_file.particles = particles
settings_file.set_source_space('box', [-32.13, -10.71, -32.13,
                                       10.71, 32.13, 10.71])
settings_file.entropy_lower_left  = [-32.13, -32.13, -32.13]
settings_file.entropy_upper_right = [ 32.13,  32.13,  32.13]
settings_file.entropy_dimension = [51, 51, 27]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [0.0, 0.0, 0.0]
plot_1.width = [64.26, 64.26]
plot_1.pixels = [500, 500]
plot_1.color = 'mat'
plot_1.basis = 'xy'

plot_2 = openmc.Plot(plot_id=2)
plot_2.filename = 'plot_2'
plot_2.origin = [0.0, 21.42, 0.0]
plot_2.width = [64.26, 64.26]
plot_2.pixels = [500, 500]
plot_2.color = 'mat'
plot_2.basis = 'xz'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.add_plot(plot_2)
plot_file.export_to_xml()
