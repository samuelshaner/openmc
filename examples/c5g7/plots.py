import openmc

###############################################################################
#                         create plots
###############################################################################

plots = {}

# Instantiate a Plot
plots['materialx-xy'] = openmc.Plot()
plots['materialx-xy'].filename = 'materials-xy'
plots['materialx-xy'].origin = [0., 0., 0.]
plots['materialx-xy'].width  = [64.26, 64.26]
plots['materialx-xy'].pixels = [1000, 1000]
plots['materialx-xy'].color = 'mat'
plots['materialx-xy'].basis = 'xy'

plots['materialx-xz'] = openmc.Plot()
plots['materialx-xz'].filename = 'materials-xz'
plots['materialx-xz'].origin = [0., 0., 0.]
plots['materialx-xz'].width = [64.26, 171.36]
plots['materialx-xz'].color = 'mat'
plots['materialx-xz'].basis = 'xz'

plots['materialx-xz-2'] = openmc.Plot()
plots['materialx-xz-2'].filename = 'materials-xz-2'
plots['materialx-xz-2'].origin = [0., 21.42, 0.]
plots['materialx-xz-2'].width = [64.26, 171.36]
plots['materialx-xz-2'].color = 'mat'
plots['materialx-xz-2'].basis = 'xz'
