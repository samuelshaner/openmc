import openmc

###############################################################################
#                 Create dictionary of common surfaces
###############################################################################

surfaces = {}

# Instantiate ZCylinder surfaces
surfaces['Core x-min'] = openmc.XPlane(surface_id=4 , x0=-80.0, name='Core x-min')
surfaces['Core y-min'] = openmc.YPlane(surface_id=5 , y0=-80.0, name='Core y-min')
surfaces['Core z-min'] = openmc.ZPlane(surface_id=6 , z0=-45.0, name='Core z-min')
surfaces['Core x-max'] = openmc.XPlane(surface_id=7 , x0= 80.0, name='Core x-max')
surfaces['Core y-max'] = openmc.YPlane(surface_id=8 , y0= 80.0, name='Core y-max')
surfaces['Core z-max'] = openmc.ZPlane(surface_id=9 , z0= 45.0, name='Core z-max')

surfaces['Core x-min'].boundary_type = 'reflective'
surfaces['Core y-min'].boundary_type = 'reflective'
surfaces['Core z-min'].boundary_type = 'reflective'
surfaces['Core x-max'].boundary_type = 'vacuum'
surfaces['Core y-max'].boundary_type = 'vacuum'
surfaces['Core z-max'].boundary_type = 'vacuum'
