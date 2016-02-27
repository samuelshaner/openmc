import openmc
from elements import *
from nuclides import *

###############################################################################
#                 Exporting to OpenMC materials.xml File
###############################################################################

pin_materials = {}

# Instantiate some Materials and register the appropriate Nuclides
UO2 = openmc.Material(name='2.46% enriched UO2')
UO2.set_density('sum')
UO2.add_nuclide(U235, 5.67505E-04, 'ao')
UO2.add_nuclide(U238, 2.22265E-02, 'ao')
UO2.add_element(O   , 4.55881E-02, 'ao')

Al_6061 = openmc.Material(name='Aluminum type 6061')
Al_6061.set_density('sum')
Al_6061.add_element(Mg, 5.34873E-04, 'ao')
Al_6061.add_element(Al, 5.80754E-02, 'ao')
Al_6061.add_element(Si, 4.63000E-04, 'ao')
Al_6061.add_element(Cr, 1.09416E-04, 'ao')
Al_6061.add_element(Mn, 4.43813E-05, 'ao')
Al_6061.add_element(Fe, 2.03741E-04, 'ao')
Al_6061.add_element(Cu, 1.02328E-04, 'ao')

B4C = openmc.Material(name='B4C for cores II-VIII')
B4C.set_density('sum')
B4C.add_element(B, 5.54982E-02, 'ao')
B4C.add_element(C, 1.33497E-02, 'ao')
B4C.add_element(O, 3.32183E-05, 'ao')

SS_304 = openmc.Material(name='304 Stainless Steel')
SS_304.set_density('sum')
SS_304.add_element(C , 2.0124E-04, 'ao')
SS_304.add_element(Mn, 1.4695E-03, 'ao')
SS_304.add_element(S , 1.5078E-05, 'ao')
SS_304.add_element(Si, 1.0035E-03, 'ao')
SS_304.add_element(Cr, 1.6772E-02, 'ao')
SS_304.add_element(Ni, 6.5966E-03, 'ao')
SS_304.add_element(Mo, 6.5504E-05, 'ao')
SS_304.add_element(Cu, 5.3252E-05, 'ao')
SS_304.add_element(Fe, 6.1838E-02, 'ao')

Gap = openmc.Material(name='Helium Gap')
Gap.set_density('sum')
Gap.add_nuclide(He4, 0.00024044, 'ao')

pin_materials['Fuel'] = UO2
pin_materials['Al']   = Al_6061
pin_materials['B4C']  = B4C
pin_materials['SS']   = SS_304
pin_materials['Gap']  = Gap

# For all core-specific materials, we'll use dictionaries to store the materials
# with the core number as the key and the material as the object. Note that not
# all cores contain certain materials (i.e only cores 8 and 14-21 have poison
# plates).
water = {}
moderator = {}
poison_plate = {}

# Water materials
water[1] = openmc.Material(name='Water, 21C for core I')
water[1].set_density('sum')
water[1].add_element(H, 6.67232E-02, 'ao')
water[1].add_element(O, 3.33616E-02, 'ao')

water[2] = openmc.Material(name='Water, 18.5C with 1037 ppm B for core II')
water[2].set_density('sum')
water[2].add_element(H, 6.67572E-02, 'ao')
water[2].add_element(O, 3.33786E-02, 'ao')
water[2].add_element(B, 5.78529E-05, 'ao')

water[3] = openmc.Material(name='Water, 18C with 764 ppm B for core III')
water[3].set_density('sum')
water[3].add_element(H, 6.67635E-02, 'ao')
water[3].add_element(O, 3.33818E-02, 'ao')
water[3].add_element(B, 4.26266E-05, 'ao')

water[4] = openmc.Material(name='Water, 17C for core IV')
water[4].set_density('sum')
water[4].add_element(H, 6.67755E-02, 'ao')
water[4].add_element(O, 3.33877E-02, 'ao')

water[5] = openmc.Material(name='Water, 17.5C for core V')
water[5].set_density('sum')
water[5].add_element(H, 6.67695E-02, 'ao')
water[5].add_element(O, 3.33848E-02, 'ao')

water[6] = openmc.Material(name='Water, 17.5C for core VI')
water[6].set_density('sum')
water[6].add_element(H, 6.67695E-02, 'ao')
water[6].add_element(O, 3.33848E-02, 'ao')

water[7] = openmc.Material(name='Water, 17.5C for core VII')
water[7].set_density('sum')
water[7].add_element(H, 6.67695E-02, 'ao')
water[7].add_element(O, 3.33848E-02, 'ao')

water[8] = openmc.Material(name='Water, 17.5C for core VIII')
water[8].set_density('sum')
water[8].add_element(H, 6.67695E-02, 'ao')
water[8].add_element(O, 3.33848E-02, 'ao')

water[9] = openmc.Material(name='Water, 17.5C for core IX')
water[9].set_density('sum')
water[9].add_element(H, 6.67695E-02, 'ao')
water[9].add_element(O, 3.33848E-02, 'ao')

water[10] = openmc.Material(name='Water, 24.5C with 143 ppm B for core X')
water[10].set_density('sum')
water[10].add_element(H, 6.66683E-02, 'ao')
water[10].add_element(O, 3.33342E-02, 'ao')
water[10].add_element(B, 7.96720E-06, 'ao')

water[11] = openmc.Material(name='Water, 26C with 514 ppm B for core XI')
water[11].set_density('sum')
water[11].add_element(H, 6.66424E-02, 'ao')
water[11].add_element(O, 3.33212E-02, 'ao')
water[11].add_element(B, 2.86260E-05, 'ao')

water[12] = openmc.Material(name='Water, 26C with 217 ppm B for core XII')
water[12].set_density('sum')
water[12].add_element(H, 6.66424E-02, 'ao')
water[12].add_element(O, 3.33212E-02, 'ao')
water[12].add_element(B, 1.20820E-05, 'ao')

water[13] = openmc.Material(name='Water, 20C with 15 ppm B for core XIII')
water[13].set_density('sum')
water[13].add_element(H, 6.67373E-02, 'ao')
water[13].add_element(O, 3.33687E-02, 'ao')
water[13].add_element(B, 8.36585E-07, 'ao')

water[14] = openmc.Material(name='Water, 18C with 92 ppm B for core XIV')
water[14].set_density('sum')
water[14].add_element(H, 6.67635E-02, 'ao')
water[14].add_element(O, 3.33813E-02, 'ao')
water[14].add_element(B, 5.13310E-06, 'ao')

water[15] = openmc.Material(name='Water, 18C with 395 ppm B for core XV')
water[15].set_density('sum')
water[15].add_element(H, 6.67635E-02, 'ao')
water[15].add_element(O, 3.33818E-02, 'ao')
water[15].add_element(B, 2.20390E-05, 'ao')

water[16] = openmc.Material(name='Water, 17.5C with 121 ppm B for core XVI')
water[16].set_density('sum')
water[16].add_element(H, 6.67695E-02, 'ao')
water[16].add_element(O, 3.33848E-02, 'ao')
water[16].add_element(B, 6.75170E-06, 'ao')

water[17] = openmc.Material(name='Water, 17.5C with 487 ppm B for core XVII')
water[17].set_density('sum')
water[17].add_element(H, 6.67695E-02, 'ao')
water[17].add_element(O, 3.33848E-02, 'ao')
water[17].add_element(B, 2.71740E-05, 'ao')

water[18] = openmc.Material(name='Water, 18C with 197 ppm B for core XVIII')
water[18].set_density('sum')
water[18].add_element(H, 6.67635E-02, 'ao')
water[18].add_element(O, 3.33818E-02, 'ao')
water[18].add_element(B, 1.09910E-05, 'ao')

water[19] = openmc.Material(name='Water, 17.5C with 634 ppm B for core XIX')
water[19].set_density('sum')
water[19].add_element(H, 6.67695E-02, 'ao')
water[19].add_element(O, 3.33848E-02, 'ao')
water[19].add_element(B, 3.53770E-05, 'ao')

water[20] = openmc.Material(name='Water, 17.5C with 320 ppm B for core XX')
water[20].set_density('sum')
water[20].add_element(H, 6.67695E-02, 'ao')
water[20].add_element(O, 3.33848E-02, 'ao')
water[20].add_element(B, 1.78560E-05, 'ao')

water[21] = openmc.Material(name='Water, 16.5C with 72 ppm B for core XXI')
water[21].set_density('sum')
water[21].add_element(H, 6.67812E-02, 'ao')
water[21].add_element(O, 3.33906E-02, 'ao')
water[21].add_element(B, 4.01830E-06, 'ao')

# Moderator materials
moderator[10] = openmc.Material(name='Moderator for core X')
moderator[10].set_density('sum')
moderator[10].add_element(H, 0.997947*6.66683E-02, 'ao')
moderator[10].add_element(O, 0.997947*3.33342E-02, 'ao')
moderator[10].add_element(B, 0.997947*7.96720E-06, 'ao')
moderator[10].add_element(Al, 1.1922E-04, 'ao')

moderator[11] = openmc.Material(name='Moderator for core XI')
moderator[11].set_density('sum')
moderator[11].add_element(H, 0.997947*6.66424E-02, 'ao')
moderator[11].add_element(O, 0.997947*3.33212E-02, 'ao')
moderator[11].add_element(B, 0.997947*2.86260E-05, 'ao')
moderator[11].add_element(Al, 1.1922E-04, 'ao')

moderator[12] = openmc.Material(name='Moderator for core XI')
moderator[12].set_density('sum')
moderator[12].add_element(H, 0.997947*6.66424E-02, 'ao')
moderator[12].add_element(O, 0.997947*3.33212E-02, 'ao')
moderator[12].add_element(B, 0.997947*1.20820E-05, 'ao')
moderator[12].add_element(Al, 1.19220E-04, 'ao')

moderator[13] = openmc.Material(name='Moderator for core XIII')
moderator[13].set_density('sum')
moderator[13].add_element(H, 0.997947*6.67373E-02, 'ao')
moderator[13].add_element(O, 0.997947*3.33687E-02, 'ao')
moderator[13].add_element(B, 0.997947*8.36585E-07, 'ao')
moderator[13].add_element(Al, 1.1922E-04, 'ao')

moderator[14] = openmc.Material(name='Moderator for core XIV')
moderator[14].set_density('sum')
moderator[14].add_element(H, 0.997947*6.67635E-02, 'ao')
moderator[14].add_element(O, 0.997947*3.33813E-02, 'ao')
moderator[14].add_element(B, 0.997947*5.13310E-06, 'ao')
moderator[14].add_element(Al, 1.1922E-04, 'ao')

moderator[15] = openmc.Material(name='Moderator for core XV')
moderator[15].set_density('sum')
moderator[15].add_element(H, 0.997947*6.67635E-02, 'ao')
moderator[15].add_element(O, 0.997947*3.33818E-02, 'ao')
moderator[15].add_element(B, 0.997947*2.20390E-05, 'ao')
moderator[15].add_element(Al, 1.1922E-04, 'ao')

moderator[16] = openmc.Material(name='Moderator for core XVI')
moderator[16].set_density('sum')
moderator[16].add_element(H, 0.997947*6.67695E-02, 'ao')
moderator[16].add_element(O, 0.997947*3.33848E-02, 'ao')
moderator[16].add_element(B, 0.997947*6.75170E-06, 'ao')
moderator[16].add_element(Al, 1.1922E-04, 'ao')

moderator[17] = openmc.Material(name='Moderator for core XVII')
moderator[17].set_density('sum')
moderator[17].add_element(H, 0.997947*6.67695E-02, 'ao')
moderator[17].add_element(O, 0.997947*3.33848E-02, 'ao')
moderator[17].add_element(B, 0.997947*2.71470E-05, 'ao')
moderator[17].add_element(Al, 1.1922E-04, 'ao')

moderator[18] = openmc.Material(name='Moderator for core XVIII')
moderator[18].set_density('sum')
moderator[18].add_element(H, 0.997947*6.67635E-02, 'ao')
moderator[18].add_element(O, 0.997947*3.33818E-02, 'ao')
moderator[18].add_element(B, 0.997947*1.09910E-05, 'ao')
moderator[18].add_element(Al, 1.1922E-04, 'ao')

moderator[19] = openmc.Material(name='Moderator for core XIX')
moderator[19].set_density('sum')
moderator[19].add_element(H, 0.997947*6.67695E-02, 'ao')
moderator[19].add_element(O, 0.997947*3.33848E-02, 'ao')
moderator[19].add_element(B, 0.997947*3.53770E-05, 'ao')
moderator[19].add_element(Al, 1.1922E-04, 'ao')

moderator[20] = openmc.Material(name='Moderator for core XX')
moderator[20].set_density('sum')
moderator[20].add_element(H, 0.997947*6.67695E-02, 'ao')
moderator[20].add_element(O, 0.997947*3.33848E-02, 'ao')
moderator[20].add_element(B, 0.997947*1.78560E-05, 'ao')
moderator[20].add_element(Al, 1.1922E-04, 'ao')

moderator[21] = openmc.Material(name='Moderator for core XXI')
moderator[21].set_density('sum')
moderator[21].add_element(H, 0.997947*6.67695E-02, 'ao')
moderator[21].add_element(O, 0.997947*3.33848E-02, 'ao')
moderator[21].add_element(B, 0.997947*4.01830E-06, 'ao')
moderator[21].add_element(Al, 1.1922E-04, 'ao')

# Poison plate materials
poison_plate[8] = openmc.Material(name='Poison plate 5 for core XIII')
poison_plate[8].set_density('sum')
poison_plate[8].add_element(B , 2.4368E-03, 'ao')
poison_plate[8].add_element(Al, 5.9382E-02, 'ao')
poison_plate[8].add_element(Fe, 4.6005E-05, 'ao')
poison_plate[8].add_element(Si, 3.4304E-05, 'ao')

poison_plate[14] = openmc.Material(name='Poison plate 4 for core XIV')
poison_plate[14].set_density('sum')
poison_plate[14].add_element(B , 1.8978E-03, 'ao')
poison_plate[14].add_element(Al, 5.9598E-02, 'ao')
poison_plate[14].add_element(Fe, 4.6172E-05, 'ao')
poison_plate[14].add_element(Si, 3.4429E-05, 'ao')

poison_plate[15] = openmc.Material(name='Poison plate 3 for cores XV')
poison_plate[15].set_density('sum')
poison_plate[15].add_element(B , 6.0543E-04, 'ao')
poison_plate[15].add_element(Al, 6.0115E-02, 'ao')
poison_plate[15].add_element(Fe, 4.6572E-05, 'ao')
poison_plate[15].add_element(Si, 3.4727E-05, 'ao')

poison_plate[16] = openmc.Material(name='Poison plate 3 for cores XVI')
poison_plate[16].set_density('sum')
poison_plate[16].add_element(B , 6.0543E-04, 'ao')
poison_plate[16].add_element(Al, 6.0115E-02, 'ao')
poison_plate[16].add_element(Fe, 4.6572E-05, 'ao')
poison_plate[16].add_element(Si, 3.4727E-05, 'ao')

poison_plate[17] = openmc.Material(name='Poison plate 2 for cores XVII')
poison_plate[17].set_density('sum')
poison_plate[17].add_element(B , 3.6537E-04, 'ao')
poison_plate[17].add_element(Al, 6.0211E-02, 'ao')
poison_plate[17].add_element(Fe, 4.6646E-05, 'ao')
poison_plate[17].add_element(Si, 3.4783E-05, 'ao')

poison_plate[18] = openmc.Material(name='Poison plate 2 for cores XVIII')
poison_plate[18].set_density('sum')
poison_plate[18].add_element(B , 3.6537E-04, 'ao')
poison_plate[18].add_element(Al, 6.0211E-02, 'ao')
poison_plate[18].add_element(Fe, 4.6646E-05, 'ao')
poison_plate[18].add_element(Si, 3.4783E-05, 'ao')

poison_plate[19] = openmc.Material(name='Poison plate 1 for cores XIX')
poison_plate[19].set_density('sum')
poison_plate[19].add_element(B , 1.5098E-04, 'ao')
poison_plate[19].add_element(Al, 6.0296E-02, 'ao')
poison_plate[19].add_element(Fe, 4.6713E-05, 'ao')
poison_plate[19].add_element(Si, 3.4832E-05, 'ao')

poison_plate[20] = openmc.Material(name='Poison plate 1 for cores XX')
poison_plate[20].set_density('sum')
poison_plate[20].add_element(B , 1.5098E-04, 'ao')
poison_plate[20].add_element(Al, 6.0296E-02, 'ao')
poison_plate[20].add_element(Fe, 4.6713E-05, 'ao')
poison_plate[20].add_element(Si, 3.4832E-05, 'ao')

poison_plate[21] = openmc.Material(name='Poison plate 1 for cores XXI')
poison_plate[21].set_density('sum')
poison_plate[21].add_element(B , 1.5098E-04, 'ao')
poison_plate[21].add_element(Al, 6.0296E-02, 'ao')
poison_plate[21].add_element(Fe, 4.6713E-05, 'ao')
poison_plate[21].add_element(Si, 3.4832E-05, 'ao')

# Instantiate a MaterialsFile, register all Materials, and export to XML
all_materials = [UO2, Al_6061, B4C, SS_304, Gap]
all_materials.extend(water.values())
all_materials.extend(moderator.values())
all_materials.extend(poison_plate.values())

materials_file = openmc.MaterialsFile()
materials_file.default_xs = '71c'
materials_file.add_materials(all_materials)
materials_file.export_to_xml()
