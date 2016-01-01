import openmc
import openmc.mgxs
import numpy as np
from universes import universes, cells

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
#                   Exporting to OpenMC geometry.xml File
###############################################################################

# Register Cells with Universe
universes['Root'].add_cells([cells['Core'], cells['Reflector'], cells['Void']])

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
settings_file.set_source_space('box', [0.0, 0.0, 0.0,
                                       15.0, 15.0, 15.0])
settings_file.entropy_lower_left = [0.0, 0.0, 0.0]
settings_file.entropy_upper_right = [25.0, 25.0, 25.0]
settings_file.entropy_dimension = [25, 25, 25]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [12.5, 12.5, 2.5]
plot_1.width = [25, 25]
plot_1.pixels = [250, 250]
plot_1.color = 'mat'
plot_1.basis = 'xy'

plot_2 = openmc.Plot(plot_id=2)
plot_2.filename = 'plot_2'
plot_2.origin = [12.5, 2.5, 12.5]
plot_2.width = [25, 25]
plot_2.pixels = [250, 250]
plot_2.color = 'mat'
plot_2.basis = 'xz'

plot_3 = openmc.Plot(plot_id=3)
plot_3.filename = 'plot_3'
plot_3.origin = [2.5, 12.5, 12.5]
plot_3.width = [25, 25]
plot_3.pixels = [250, 250]
plot_3.color = 'mat'
plot_3.basis = 'yz'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.add_plot(plot_2)
plot_file.add_plot(plot_3)
plot_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################

# Instantiate a tally mesh
#mesh = openmc.Mesh(mesh_id=1)
#mesh.type = 'regular'
#mesh.dimension = [25, 25, 25]
#mesh.lower_left = [0.0, 0.0, 0.0]
#mesh.upper_right = [25.0, 25.0, 25.0]

# Instantiate some tally Filters
#energy_filter = openmc.Filter(type='energy',
#                              bins=[1E-11, 4.0E-6, 20.0])
#mesh_filter = openmc.Filter()
#mesh_filter.mesh = mesh

# Instantiate the Tally
#tally = openmc.Tally(tally_id=1, name='tally 1')
#tally.add_filter(energy_filter)
#tally.add_filter(mesh_filter)
#tally.add_score('flux')
#tally.add_score('fission')
#tally.add_score('nu-fission')

# Instantiate a TalliesFile, register all Tallies, and export to XML
#tallies_file = openmc.TalliesFile()
#tallies_file.add_mesh(mesh)
#tallies_file.add_tally(tally)
#tallies_file.export_to_xml()
