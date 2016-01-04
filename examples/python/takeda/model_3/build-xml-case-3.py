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

# Create the root lattice
lattices['Root'] = openmc.RectLattice(lattice_id=201, name='Root')
lattices['Root'].dimension = [1, 1, 18]
lattices['Root'].lower_left = [-80.0, -80.0, -45.0]
lattices['Root'].pitch = [160.0, 160.0, 5.0]
ibr = universes['Internal Blanket Rodded']
ibu = universes['Internal Blanket Unrodded']
ibf = universes['Internal Blanket Filled']
cr  = universes['Core Rodded']
cu  = universes['Core Unrodded']
cf  = universes['Core Filled']
abu = universes['Axial Blanket Unrodded']
abf = universes['Axial Blanket Filled']
aru = universes['Axial Reflector Unrodded']
arf = universes['Axial Reflector Filled']
lattices['Root'].universes = [[[ibf]]]*2 + [[[cf]]]*9 + [[[abf]]]*5 + [[[arf]]]*2
cells['Root'].fill         = lattices['Root']

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
settings_file.set_source_space('box', [-80.0, -80.0, -45.0,
                                        40.0,  40.0,  10.0])
settings_file.entropy_lower_left  = [-80.0, -80.0, -45.0]
settings_file.entropy_upper_right = [ 80.0,  80.0,  45.0]
settings_file.entropy_dimension = [32, 32, 18]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [0.0, 0.0, -40.0]
plot_1.width = [160.0, 160.0]
plot_1.pixels = [500, 500]
plot_1.color = 'mat'
plot_1.basis = 'xy'

plot_2 = openmc.Plot(plot_id=2)
plot_2.filename = 'plot_2'
plot_2.origin = [0.0, -78.5, 0.0]
plot_2.width = [160.0, 90.0]
plot_2.pixels = [500, 500]
plot_2.color = 'mat'
plot_2.basis = 'xz'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.add_plot(plot_2)
plot_file.export_to_xml()
