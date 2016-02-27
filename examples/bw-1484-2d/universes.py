import openmc
from cells import cells, surfaces

###############################################################################
#                     Create a dictionary of all shared universes
###############################################################################

# Instantiate Universes
universes = {}

universes['Fuel Rod Core 1']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 2']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 3']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 4']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 5']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 6']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 7']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 8']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 9']             = openmc.Universe(universe_id=1,  name='Fuel Rod')
universes['Fuel Rod Core 10']            = openmc.Universe(universe_id=1,  name='Fuel Rod')


universes['Al Rod Core 1']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 2']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 3']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 4']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 5']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 6']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 7']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 8']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 9']               = openmc.Universe(universe_id=2,  name='Al Rod')
universes['Al Rod Core 10']              = openmc.Universe(universe_id=2,  name='Al Rod')

universes['B4C Rod Core 1']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 2']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 3']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 4']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 5']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 6']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 7']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 8']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 9']              = openmc.Universe(universe_id=3,  name='B4C Rod')
universes['B4C Rod Core 10']             = openmc.Universe(universe_id=3,  name='B4C Rod')

universes['Reflector Core 1']            = openmc.Universe(universe_id=4,  name='Reflector Core 1')
universes['Reflector Core 2']            = openmc.Universe(universe_id=4,  name='Reflector Core 2')
universes['Reflector Core 3']            = openmc.Universe(universe_id=4,  name='Reflector Core 3')
universes['Reflector Core 4']            = openmc.Universe(universe_id=4,  name='Reflector Core 4')
universes['Reflector Core 5']            = openmc.Universe(universe_id=4,  name='Reflector Core 5')
universes['Reflector Core 6']            = openmc.Universe(universe_id=4,  name='Reflector Core 6')
universes['Reflector Core 7']            = openmc.Universe(universe_id=4,  name='Reflector Core 7')
universes['Reflector Core 8']            = openmc.Universe(universe_id=4,  name='Reflector Core 8')
universes['Reflector Core 9']            = openmc.Universe(universe_id=4,  name='Reflector Core 9')
universes['Reflector Core 10']           = openmc.Universe(universe_id=4,  name='Reflector Core 10')

universes['Root Core 1']                 = openmc.Universe(universe_id=0,  name='Root Core 1')
universes['Root Core 2']                 = openmc.Universe(universe_id=0,  name='Root Core 2')
universes['Root Core 3']                 = openmc.Universe(universe_id=0,  name='Root Core 3')
universes['Root Core 4']                 = openmc.Universe(universe_id=0,  name='Root Core 4')
universes['Root Core 5']                 = openmc.Universe(universe_id=0,  name='Root Core 5')
universes['Root Core 6']                 = openmc.Universe(universe_id=0,  name='Root Core 6')
universes['Root Core 7']                 = openmc.Universe(universe_id=0,  name='Root Core 7')
universes['Root Core 8']                 = openmc.Universe(universe_id=0,  name='Root Core 8')
universes['Root Core 9']                 = openmc.Universe(universe_id=0,  name='Root Core 9')
universes['Root Core 10']                = openmc.Universe(universe_id=0,  name='Root Core 10')

# Register Cells with Universes
universes['Root Core 1']      .add_cell(cells['Core 1'])
universes['Root Core 2']      .add_cell(cells['Core 2'])
universes['Root Core 3']      .add_cell(cells['Core 3'])
universes['Root Core 4']      .add_cell(cells['Core 4'])
universes['Root Core 5']      .add_cell(cells['Core 5'])
universes['Root Core 6']      .add_cell(cells['Core 6'])
universes['Root Core 7']      .add_cell(cells['Core 7'])
universes['Root Core 8']      .add_cell(cells['Core 8'])
universes['Root Core 9']      .add_cell(cells['Core 9'])
universes['Root Core 10']     .add_cell(cells['Core 10'])


universes['Fuel Rod Core 1']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 1']])
universes['Fuel Rod Core 2']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 2']])
universes['Fuel Rod Core 3']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 3']])
universes['Fuel Rod Core 4']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 4']])
universes['Fuel Rod Core 5']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 5']])
universes['Fuel Rod Core 6']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 6']])
universes['Fuel Rod Core 7']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 7']])
universes['Fuel Rod Core 8']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 8']])
universes['Fuel Rod Core 9']  .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 9']])
universes['Fuel Rod Core 10'] .add_cells([cells['Fuel Rod Fuel'], cells['Fuel Rod Gap'],
                                   cells['Fuel Rod Clad'], cells['Fuel Rod Moderator Core 10']])

universes['Al Rod Core 1']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 1']])
universes['Al Rod Core 2']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 2']])
universes['Al Rod Core 3']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 3']])
universes['Al Rod Core 4']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 4']])
universes['Al Rod Core 5']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 5']])
universes['Al Rod Core 6']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 6']])
universes['Al Rod Core 7']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 7']])
universes['Al Rod Core 8']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 8']])
universes['Al Rod Core 9']    .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 9']])
universes['Al Rod Core 10']   .add_cells([cells['Al Rod Al'], cells['Al Rod Moderator Core 10']])

universes['B4C Rod Core 1']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 1']])
universes['B4C Rod Core 2']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 2']])
universes['B4C Rod Core 3']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 3']])
universes['B4C Rod Core 4']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 4']])
universes['B4C Rod Core 5']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 5']])
universes['B4C Rod Core 6']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 6']])
universes['B4C Rod Core 7']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 7']])
universes['B4C Rod Core 8']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 8']])
universes['B4C Rod Core 9']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                          cells['B4C Rod Moderator Core 9']])
universes['B4C Rod Core 10']   .add_cells([cells['B4C Rod B4C'], cells['B4C Rod Clad'],
                                           cells['B4C Rod Moderator Core 10']])

universes['Reflector Core 1'] .add_cell(cells['Reflector Core 1'])
universes['Reflector Core 2'] .add_cell(cells['Reflector Core 2'])
universes['Reflector Core 3'] .add_cell(cells['Reflector Core 3'])
universes['Reflector Core 4'] .add_cell(cells['Reflector Core 4'])
universes['Reflector Core 5'] .add_cell(cells['Reflector Core 5'])
universes['Reflector Core 6'] .add_cell(cells['Reflector Core 6'])
universes['Reflector Core 7'] .add_cell(cells['Reflector Core 7'])
universes['Reflector Core 8'] .add_cell(cells['Reflector Core 8'])
universes['Reflector Core 9'] .add_cell(cells['Reflector Core 9'])
universes['Reflector Core 10'].add_cell(cells['Reflector Core 10'])
