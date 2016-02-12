import openmc
from cells import cells

###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################

tallies = {}

# Instantiate a distribcell Tally
tallies['UO2'] = openmc.Tally(tally_id=1)
tallies['UO2'].add_filter(openmc.Filter(type='distribcell', bins=[cells['UO2'].id]))
tallies['UO2'].add_score('fission')

tallies['MOX 4.3%'] = openmc.Tally(tally_id=2)
tallies['MOX 4.3%'].add_filter(openmc.Filter(type='distribcell', bins=[cells['MOX 4.3%'].id]))
tallies['MOX 4.3%'].add_score('fission')

tallies['MOX 7.0%'] = openmc.Tally(tally_id=3)
tallies['MOX 7.0%'].add_filter(openmc.Filter(type='distribcell', bins=[cells['MOX 7.0%'].id]))
tallies['MOX 7.0%'].add_score('fission')

tallies['MOX 8.7%'] = openmc.Tally(tally_id=4)
tallies['MOX 8.7%'].add_filter(openmc.Filter(type='distribcell', bins=[cells['MOX 8.7%'].id]))
tallies['MOX 8.7%'].add_score('fission')

tallies['Fission Chamber'] = openmc.Tally(tally_id=5)
tallies['Fission Chamber'].add_filter(openmc.Filter(type='distribcell', bins=[cells['Fission Chamber'].id]))
tallies['Fission Chamber'].add_score('fission')
