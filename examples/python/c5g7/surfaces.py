import openmc

###############################################################################
#                     Create a dictionary of all shared cells
###############################################################################

# Create a dictionary to store the surfaces
surfaces = {}

# Instantiate Pin Cell ZCylinder surface
surfaces['Pin Cell ZCylinder'] = openmc.ZCylinder(surface_id=1, x0=0, y0=0, R=0.54, name='Pin Cell ZCylinder')
