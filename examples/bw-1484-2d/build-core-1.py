import openmc
from openmc.source import Source
from openmc.stats import Box

from lattices import universes

###############################################################################
#                      Simulation Input File Parameters
###############################################################################

# OpenMC simulation parameters
batches = 100
inactive = 10
particles = 1000



###############################################################################
#                 Exporting to OpenMC geometry.xml File
###############################################################################


# Instantiate a Geometry and register the root Universe
geometry = openmc.Geometry()
geometry.root_universe = universes['Root Core 1']

# Instantiate a GeometryFile, register Geometry, and export to XML
geometry_file = openmc.GeometryFile()
geometry_file.geometry = geometry
geometry_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC settings.xml File
###############################################################################

# Instantiate a SettingsFile, set all runtime parameters, and export to XML
settings_file = openmc.SettingsFile()
settings_file.batches = batches
settings_file.inactive = inactive
settings_file.particles = particles
settings_file.source = Source(space=Box([-1.636*12, -1.636*12, -1],
                                        [1.636*12 ,  1.636*12,  1]))
settings_file.entropy_lower_left = [-1.636*39, -1.636*39, -1.e50]
settings_file.entropy_upper_right = [1.636*39, 1.636*39, 1.e50]
settings_file.entropy_dimension = [78, 78, 1]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################

# Instantiate a tally mesh
mesh = openmc.Mesh(mesh_id=1)
mesh.type = 'regular'
mesh.dimension = [78, 78, 1]
mesh.lower_left = [-1.636*39, -1.636*39, -1.e50]
mesh.upper_right = [1.636*39, 1.636*39, 1.e50]

# Instantiate some tally Filters
energy_filter = openmc.Filter(type='energy', bins=[0., 4.e-6, 20.])
mesh_filter = openmc.Filter()
mesh_filter.mesh = mesh

# Instantiate the Tally
tally_1 = openmc.Tally(tally_id=1, name='tally 1')
tally_1.add_filter(energy_filter)
tally_1.add_filter(mesh_filter)
tally_1.add_score('flux')
tally_1.add_score('fission')
tally_1.add_score('nu-fission')

# Instantiate the Tally
#cell_filter = openmc.Filter(type='cell', bins=[1,2,3,4,10])
#tally_2 = openmc.Tally(tally_id=2, name='tally 2')
#tally_2.add_filter(energy_filter)
#tally_2.add_filter(cell_filter)
#tally_2.add_score('transport')
#tally_2.add_score('nu-scatter')
#tally_2.add_score('nu-fission')

# Instantiate a TalliesFile, register all Tallies, and export to XML
tallies_file = openmc.TalliesFile()
#tallies_file.add_tally(tally_2)
tallies_file.add_tally(tally_1)
tallies_file.add_mesh(mesh)
tallies_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [0.0, 0.0, 1.0]
plot_1.width = [1.636*78, 1.636*78]
plot_1.pixels = [1000, 1000]
plot_1.color = 'mat'
plot_1.basis = 'xy'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.export_to_xml()
