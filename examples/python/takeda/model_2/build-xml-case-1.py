import openmc
from lattices import lattices, universes, cells
from openmc.source import Source
from openmc.stats import Box

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
lattices['Root'] = openmc.RectLattice(lattice_id=105, name='Root')
lattices['Root'].dimension = [1, 1, 30]
lattices['Root'].lower_left = [-35.0, -35.0, -75.0]
lattices['Root'].pitch = [70.0, 70.0, 5.0]
cu = universes['Core Upper']
cl = universes['Core Lower']
bu = universes['Blanket Upper']
bl = universes['Blanket Lower']
lattices['Root'].universes = [[[bl]]]*4 + [[[cl]]]*22 + [[[bl]]]*4
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
settings_file.source = Source(space=Box([-35.0, -35.0, -75.0],
                                        [35.0,  35.0,  75.0]))
settings_file.entropy_lower_left  = [-35.0, -35.0, -75.0]
settings_file.entropy_upper_right = [ 35.0,  35.0,  75.0]
settings_file.entropy_dimension = [14, 14, 30]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [0.0, 0.0, -25.0]
plot_1.width = [70.0, 70.0]
plot_1.pixels = [500, 500]
plot_1.color = 'mat'
plot_1.basis = 'xy'

plot_2 = openmc.Plot(plot_id=2)
plot_2.filename = 'plot_2'
plot_2.origin = [0.0, -32.5, 0.0]
plot_2.width = [70.0, 150.0]
plot_2.pixels = [500, 500]
plot_2.color = 'mat'
plot_2.basis = 'xz'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.add_plot(plot_2)
plot_file.export_to_xml()
