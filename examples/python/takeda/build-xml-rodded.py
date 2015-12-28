import openmc
import openmc.mgxs
import numpy as np

###############################################################################
#                      Simulation Input File Parameters
###############################################################################

# OpenMC simulation parameters
batches = 200
inactive = 100
particles = 10000

###############################################################################
#                 Exporting to OpenMC mg_cross_sections.xml File
###############################################################################

# Instantiate the energy group data
groups = openmc.mgxs.EnergyGroups(group_edges=[1E-11, 6.8256E-7, 10.0])

# Instantiate the 2-group (Takeda) cross section data
core_xsdata = openmc.Xsdata('core.300k', groups)
core_xsdata.order = 0
core_xsdata.total = np.array([0.223775, 1.03864])
core_xsdata.absorption = np.array([0.00852709, 0.158196])
scatter = [[[0.192423, 0.0228253], [0.0, 0.880439]]]
core_xsdata.scatter = np.array(scatter[:][:])
core_xsdata.fission = np.array([0.0004, 0.1])
core_xsdata.nu_fission = np.array([0.00909319, 0.290183])
core_xsdata.chi = np.array([1.0, 0.0])

refl_xsdata = openmc.Xsdata('refl.300k', groups)
refl_xsdata.order = 0
refl_xsdata.total = np.array([0.250367, 1.64482])
refl_xsdata.absorption = np.array([0.000416392, 0.0202999])
scatter = [[[0.193446, 0.0565042], [0.00, 1.62452]]]
refl_xsdata.scatter = np.array(scatter[:][:])
refl_xsdata.fission = np.array([0.0, 0.0])
refl_xsdata.nu_fission = np.array([0.0, 0.0])
refl_xsdata.chi = np.array([1.0, 0.0])

control_rod_xsdata = openmc.Xsdata('control_rod.300k', groups)
control_rod_xsdata.order = 0
control_rod_xsdata.total = np.array([0.0852325, 0.217460])
control_rod_xsdata.absorption = np.array([0.0174439, 0.182224])
scatter = [[[0.0677241, 0.0000645461], [0.00, 0.0352358]]]
control_rod_xsdata.scatter = np.array(scatter[:][:])
control_rod_xsdata.fission = np.array([0.0, 0.0])
control_rod_xsdata.nu_fission = np.array([0.0, 0.0])
control_rod_xsdata.chi = np.array([1.0, 0.0])

void_xsdata = openmc.Xsdata('void.300k', groups)
void_xsdata.order = 0
void_xsdata.total = np.array([0.0128407, 0.0120676])
void_xsdata.absorption = np.array([0.0000465132, 0.00132890])
scatter = [[[0.01277, 0.0000240997], [0.00, 0.0107387]]]
void_xsdata.scatter = np.array(scatter[:][:])
void_xsdata.fission = np.array([0.0, 0.0])
void_xsdata.nu_fission = np.array([0.0, 0.0])
void_xsdata.chi = np.array([1.0, 0.0])

mg_cross_sections_file = openmc.MGXSLibraryFile(groups)
mg_cross_sections_file.add_xsdatas([core_xsdata, refl_xsdata,
                                    control_rod_xsdata, void_xsdata])
mg_cross_sections_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC materials.xml File
###############################################################################

# Instantiate some Macroscopic Data
core_data = openmc.Macroscopic('core', '300k')
refl_data = openmc.Macroscopic('refl', '300k')
control_rod_data = openmc.Macroscopic('control_rod', '300k')
void_data = openmc.Macroscopic('void', '300k')

# Instantiate some Materials and register the appropriate Nuclides
core = openmc.Material(material_id=1, name='Core fuel')
core.set_density('macro', 1.0)
core.add_macroscopic(core_data)

refl = openmc.Material(material_id=2, name='Reflector')
refl.set_density('macro', 1.0)
refl.add_macroscopic(refl_data)

control_rod = openmc.Material(material_id=3, name='Control Rod')
control_rod.set_density('macro', 1.0)
control_rod.add_macroscopic(control_rod_data)

void = openmc.Material(material_id=4, name='Void')
void.set_density('macro', 1.0)
void.add_macroscopic(void_data)

# Instantiate a MaterialsFile, register all Materials, and export to XML
materials_file = openmc.MaterialsFile()
materials_file.default_xs = '300k'
materials_file.add_materials([core, refl, control_rod, void])
materials_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC geometry.xml File
###############################################################################

# Instantiate ZCylinder surfaces
fuel_x_max = openmc.XPlane(surface_id=1, x0=15.0, name='Fuel x-max')
fuel_y_max = openmc.YPlane(surface_id=2, y0=15.0, name='Fuel y-max')
fuel_z_max = openmc.ZPlane(surface_id=3, z0=15.0, name='Fuel z-max')

core_x_min = openmc.XPlane(surface_id=4, x0=0.0, name='Core x-min')
core_y_min = openmc.YPlane(surface_id=5, y0=0.0, name='Core y-min')
core_z_min = openmc.ZPlane(surface_id=6, z0=0.0, name='Core z-min')
core_x_max = openmc.XPlane(surface_id=7, x0=25.0, name='Core x-max')
core_y_max = openmc.YPlane(surface_id=8, y0=25.0, name='Core y-max')
core_z_max = openmc.ZPlane(surface_id=9, z0=25.0, name='Core z-max')

void_x_max = openmc.XPlane(surface_id=10, x0=20.0, name='Void x-max')
void_y_max = openmc.YPlane(surface_id=11, y0=5.0, name='Void y-max')

core_x_min.boundary_type = 'reflective'
core_y_min.boundary_type = 'reflective'
core_z_min.boundary_type = 'reflective'
core_x_max.boundary_type = 'vacuum'
core_y_max.boundary_type = 'vacuum'
core_z_max.boundary_type = 'vacuum'

# Instantiate Cells
fuel_cell = openmc.Cell(cell_id=1, name='cell 1')
control_rod_cell = openmc.Cell(cell_id=2, name='cell 2')
refl_cell = openmc.Cell(cell_id=3, name='cell 3')
#refl_cell_1 = openmc.Cell(cell_id=3, name='cell 3')
#refl_cell_2 = openmc.Cell(cell_id=4, name='cell 4')
#refl_cell_3 = openmc.Cell(cell_id=5, name='cell 5')
#refl_cell_4 = openmc.Cell(cell_id=6, name='cell 6')

# Use surface half-spaces to define regions
fuel_cell.region = +core_x_min & +core_y_min & +core_z_min & -fuel_x_max & -fuel_y_max & -fuel_z_max
control_rod_cell.region = +fuel_x_max & -void_x_max & +core_y_min & -void_y_max & +core_z_min & -core_z_max
refl_cell.region = ~fuel_cell.region & ~control_rod_cell.region & +core_x_min & +core_y_min & +core_z_min & -core_x_max & -core_y_max & -core_z_max
#refl_cell_1.region = +core_x_min & -fuel_x_max & +fuel_y_max & -core_y_max & +core_z_min & -core_z_max
#refl_cell_2.region = +fuel_x_max & -void_x_max & +void_y_max & -core_y_max & +core_z_min & -core_z_max
#refl_cell_3.region = +void_x_max & -core_x_max & +core_y_min & -core_y_max & +core_z_min & -core_z_max
#refl_cell_4.region = +core_x_min & -fuel_x_max & +core_y_min & -fuel_y_max & +fuel_z_max & -core_z_max

# Register Materials with Cells
fuel_cell.fill = core
control_rod_cell.fill = control_rod
refl_cell.fill = refl

# Instantiate Universe
root = openmc.Universe(universe_id=0, name='root universe')

# Register Cells with Universe
root.add_cells([fuel_cell, control_rod_cell, refl_cell])

# Instantiate a Geometry and register the root Universe
geometry = openmc.Geometry()
geometry.root_universe = root

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
