import openmc
import openmc.mgxs
import numpy as np

###############################################################################
#                 Exporting to OpenMC mg_cross_sections.xml File
###############################################################################

# Instantiate the energy group data
groups = openmc.mgxs.EnergyGroups(group_edges=[1E-11, 9.6122E-04, 8.6517E-02, 1.3534E-00, 1.E1])

# Instantiate the 4-group (Takeda) cross section data
core_xsdata = openmc.Xsdata('core.300k', groups)
core_xsdata.order = 0
core_xsdata.total      = np.array([1.14568E-01, 2.05177E-01, 3.29381E-01, 3.89810E-01])
core_xsdata.absorption = np.array([7.45551E-03, 3.5254E-03, 7.80136E-03, 2.74496E-02])
core_xsdata.scatter    = np.array([[[7.04326E-02, 3.47967E-02, 1.88282E-03, 0.00000E-00],
                                    [0.00000E-00, 1.95443E-01, 6.20863E-03, 7.07208E-07],
                                    [0.00000E-00, 0.00000E-00, 3.20586E-01, 9.92975E-04],
                                    [0.00000E-00, 0.00000E-00, 0.00000E-00, 3.62360E-01]]])
core_xsdata.nu_fission = np.array([2.06063E-02, 6.10571E-03, 6.91403E-03, 2.60689E-02])
core_xsdata.fission    = np.array([2.06063E-02, 6.10571E-03, 6.91403E-03, 2.60689E-02]) * 0.5
core_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

axial_reflector_xsdata = openmc.Xsdata('axial_reflector.300k', groups)
axial_reflector_xsdata.order = 0
axial_reflector_xsdata.total      = np.array([1.65612E-01, 1.66866E-01, 2.68633E-01, 8.34911E-01])
axial_reflector_xsdata.absorption = np.array([6.39154E-04, 4.06876E-04, 1.20472E-03, 4.36382E-03])
axial_reflector_xsdata.scatter    = np.array([[[1.15653E-01, 4.84731E-02, 8.46495E-04, 0.00000E-00],
                                               [0.00000E-00, 1.60818E-01, 5.64096E-03, 6.57573E-07],
                                               [0.00000E-00, 0.00000E-00, 2.65011E-01, 2.41755E-03],
                                               [0.00000E-00, 0.00000E-00, 0.00000E-00, 8.30547E-01]]])
axial_reflector_xsdata.nu_fission = np.array([0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00])
axial_reflector_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

radial_inner_blanket_xsdata = openmc.Xsdata('radial_inner_blanket.300k', groups)
radial_inner_blanket_xsdata.order = 0
radial_inner_blanket_xsdata.total      = np.array([1.19648E-01, 2.42195E-01, 3.56476E-01, 3.79433E-01])
radial_inner_blanket_xsdata.absorption = np.array([7.43283E-03, 1.99906E-03, 6.79036E-03, 1.58015E-02])
radial_inner_blanket_xsdata.scatter    = np.array([[[6.91158E-02, 4.04132E-02, 2.68621E-03, 0.00000E-00],
                                                    [0.00000E-00, 2.30626E-01, 9.57027E-03, 1.99571E-07],
                                                    [0.00000E-00, 0.00000E-00, 3.48414E-01, 1.27195E-03],
                                                    [0.00000E-00, 0.00000E-00, 0.00000E-00, 3.63631E-01]]])
radial_inner_blanket_xsdata.nu_fission = np.array([1.89496E-02, 1.75265E-04, 2.06978E-04, 1.13451E-03])
radial_inner_blanket_xsdata.fission    = np.array([1.89496E-02, 1.75265E-04, 2.06978E-04, 1.13451E-03]) * 0.5
radial_inner_blanket_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

radial_reflector_xsdata = openmc.Xsdata('radial_reflector.300k', groups)
radial_reflector_xsdata.order = 0
radial_reflector_xsdata.total      = np.array([1.71748E-01, 2.17826E-01, 4.47761E-01, 7.95199E-01])
radial_reflector_xsdata.absorption = np.array([1.13305E-03, 4.90793E-04, 1.94500E-03, 5.70263E-03])
radial_reflector_xsdata.scatter    = np.array([[[1.23352E-01, 4.61307E-02, 1.13217E-03, 0.00000E-00],
                                                [0.00000E-00, 2.11064E-01, 6.27100E-03, 1.03831E-06],
                                                [0.00000E-00, 0.00000E-00, 4.43045E-01, 2.77126E-03],
                                                [0.00000E-00, 0.00000E-00, 0.00000E-00, 7.89497E-01]]])
radial_reflector_xsdata.nu_fission = np.array([0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00])
radial_reflector_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

axial_blanket_xsdata = openmc.Xsdata('axial_blanket.300k', groups)
axial_blanket_xsdata.order = 0
axial_blanket_xsdata.total      = np.array([1.16493E-01, 2.20521E-01, 3.44544E-01, 3.88356E-01])
axial_blanket_xsdata.absorption = np.array([5.35418E-03, 1.48604E-03, 5.35300E-03, 1.34694E-02])
axial_blanket_xsdata.scatter    = np.array([[[7.16044E-02, 3.73170E-02, 2.21707E-03, 0.00000E-00],
                                             [0.00000E-00, 2.10436E-01, 8.59855E-03, 6.68299E-07],
                                             [0.00000E-00, 0.00000E-00, 3.37506E-01, 1.68530E-03],
                                             [0.00000E-00, 0.00000E-00, 0.00000E-00, 3.74866E-01]]])
axial_blanket_xsdata.nu_fission = np.array([1.31770E-02, 1.26026E-04, 1.52380E-04, 7.87302E-04])
axial_blanket_xsdata.fission    = np.array([1.31770E-02, 1.26026E-04, 1.52380E-04, 7.87302E-04]) * 0.5
axial_blanket_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

control_rod_xsdata = openmc.Xsdata('control_rod.300k', groups)
control_rod_xsdata.order = 0
control_rod_xsdata.total      = np.array([1.84333E-01, 3.66121E-01, 6.15527E-01, 1.09486E-00])
control_rod_xsdata.absorption = np.array([5.97638E-03, 1.76941E-02, 8.82741E-02, 4.75591E-01])
control_rod_xsdata.scatter    = np.array([[[1.34373E-01, 4.37775E-02, 2.06054E-04, 0.00000E-00],
                                           [0.00000E-00, 3.18582E-01, 2.98432E-02, 8.71188E-07],
                                           [0.00000E-00, 0.00000E-00, 5.19591E-01, 7.66209E-03],
                                           [0.00000E-00, 0.00000E-00, 0.00000E-00, 6.18265E-01]]])
control_rod_xsdata.nu_fission = np.array([0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00])
control_rod_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

na_filled_crp_xsdata = openmc.Xsdata('na_filled_crp.300k', groups)
na_filled_crp_xsdata.order = 0
na_filled_crp_xsdata.total      = np.array([6.58979E-02, 1.09810E-01, 1.86765E-01, 2.09933E-01])
na_filled_crp_xsdata.absorption = np.array([3.10744E-04, 1.13062E-04, 4.48988E-04, 1.07518E-03])
na_filled_crp_xsdata.scatter    = np.array([[[4.74407E-02, 1.76894E-02, 4.57012E-04, 0.00000E-00],
                                             [0.00000E-00, 1.06142E-01, 3.55466E-03, 1.77599E-07],
                                             [0.00000E-00, 0.00000E-00, 1.85304E-01, 1.01280E-03],
                                             [0.00000E-00, 0.00000E-00, 0.00000E-00, 2.08858E-01]]])
na_filled_crp_xsdata.nu_fission = np.array([0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00])
na_filled_crp_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

empty_matrix_xsdata = openmc.Xsdata('empty_matrix.300k', groups)
empty_matrix_xsdata.order = 0
empty_matrix_xsdata.total      = np.array([1.36985E-02, 1.69037E-02, 3.12271E-02, 6.29537E-02])
empty_matrix_xsdata.absorption = np.array([7.49800E-05, 3.82435E-05, 1.39355E-04, 4.95515E-04])
empty_matrix_xsdata.scatter    = np.array([[[9.57999E-03, 3.95552E-03, 8.80428E-05, 0.00000E-00],
                                            [0.00000E-00, 1.64740E-02, 3.91394E-04, 7.72254E-08],
                                            [0.00000E-00, 0.00000E-00, 3.09104E-02, 1.77293E-04],
                                            [0.00000E-00, 0.00000E-00, 0.00000E-00, 6.24581E-02]]])
empty_matrix_xsdata.nu_fission = np.array([0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00])
empty_matrix_xsdata.chi        = np.array([5.83319E-01, 4.05450E-01, 1.12310E-02, 0.00000E-00])

mg_cross_sections_file = openmc.MGXSLibraryFile(groups)
mg_cross_sections_file.add_xsdatas([core_xsdata, axial_reflector_xsdata,
                                    radial_inner_blanket_xsdata, radial_reflector_xsdata,
                                    axial_blanket_xsdata, control_rod_xsdata,
                                    na_filled_crp_xsdata, empty_matrix_xsdata])
mg_cross_sections_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC materials.xml File
###############################################################################

# Instantiate some Macroscopic Data
core_data = openmc.Macroscopic('core', '300k')
axial_reflector_data = openmc.Macroscopic('axial_reflector', '300k')
radial_inner_blanket_data = openmc.Macroscopic('radial_inner_blanket', '300k')
radial_reflector_data = openmc.Macroscopic('radial_reflector', '300k')
axial_blanket_data = openmc.Macroscopic('axial_blanket', '300k')
control_rod_data = openmc.Macroscopic('control_rod', '300k')
na_filled_crp_data = openmc.Macroscopic('na_filled_crp', '300k')
empty_matrix_data = openmc.Macroscopic('empty_matrix', '300k')

# Instantiate Materials dictionary
materials = {}

# Instantiate some Materials and register the appropriate Nuclides
materials['Core'] = openmc.Material(material_id=1, name='Core')
materials['Core'].set_density('macro', 1.0)
materials['Core'].add_macroscopic(core_data)

materials['Axial Reflector'] = openmc.Material(material_id=2, name='Axial Reflector')
materials['Axial Reflector'].set_density('macro', 1.0)
materials['Axial Reflector'].add_macroscopic(axial_reflector_data)

materials['Radial & Inner Blanket'] = openmc.Material(material_id=3, name='Radial & Inner Blanket')
materials['Radial & Inner Blanket'].set_density('macro', 1.0)
materials['Radial & Inner Blanket'].add_macroscopic(radial_inner_blanket_data)

materials['Radial Reflector'] = openmc.Material(material_id=4, name='Radial Reflector')
materials['Radial Reflector'].set_density('macro', 1.0)
materials['Radial Reflector'].add_macroscopic(radial_reflector_data)

materials['Axial Blanket'] = openmc.Material(material_id=5, name='Axial Blanket')
materials['Axial Blanket'].set_density('macro', 1.0)
materials['Axial Blanket'].add_macroscopic(axial_blanket_data)

materials['Control Rod'] = openmc.Material(material_id=6, name='Control Rod')
materials['Control Rod'].set_density('macro', 1.0)
materials['Control Rod'].add_macroscopic(control_rod_data)

materials['Na Filled CRP'] = openmc.Material(material_id=7, name='Na Filled CRP')
materials['Na Filled CRP'].set_density('macro', 1.0)
materials['Na Filled CRP'].add_macroscopic(na_filled_crp_data)

materials['Empty Matrix'] = openmc.Material(material_id=8, name='Empty Matrix')
materials['Empty Matrix'].set_density('macro', 1.0)
materials['Empty Matrix'].add_macroscopic(empty_matrix_data)
