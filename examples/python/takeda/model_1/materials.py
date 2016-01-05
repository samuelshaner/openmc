import openmc
import numpy as np
import openmc.mgxs

###############################################################################
#                 Create dictionary of materials
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
core_xsdata.fission = np.array([0.00909319, 0.290183]) * 0.5
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

# Instantiate some Macroscopic Data
core_data = openmc.Macroscopic('core', '300k')
refl_data = openmc.Macroscopic('refl', '300k')
control_rod_data = openmc.Macroscopic('control_rod', '300k')
void_data = openmc.Macroscopic('void', '300k')

# Create dictionary of materials
materials = {}

# Instantiate some Materials and register the appropriate Nuclides
materials['Core'] = openmc.Material(material_id=1, name='Core')
materials['Core'].set_density('macro', 1.0)
materials['Core'].add_macroscopic(core_data)

materials['Reflector'] = openmc.Material(material_id=2, name='Reflector')
materials['Reflector'].set_density('macro', 1.0)
materials['Reflector'].add_macroscopic(refl_data)

materials['Control Rod'] = openmc.Material(material_id=3, name='Control Rod')
materials['Control Rod'].set_density('macro', 1.0)
materials['Control Rod'].add_macroscopic(control_rod_data)

materials['Void'] = openmc.Material(material_id=4, name='Void')
materials['Void'].set_density('macro', 1.0)
materials['Void'].add_macroscopic(void_data)
