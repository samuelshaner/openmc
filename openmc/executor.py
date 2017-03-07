from __future__ import print_function
import subprocess
from numbers import Integral

from six import string_types

from openmc import VolumeCalculation

def _run(command, output, cwd):
    # Launch a subprocess
    p = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, universal_newlines=True)

    # Capture and re-print OpenMC output in real-time
    while True:
        # If OpenMC is finished, break loop
        line = p.stdout.readline()
        if not line and p.poll() is not None:
            break

        if output:
            # If user requested output, print to screen
            print(line, end='')

    # Return the returncode (integer, zero if no problems encountered)
    return p.returncode


def plot_geometry(output=True, openmc_exec='openmc', cwd='.'):
    """Run OpenMC in plotting mode

    Parameters
    ----------
    output : bool
        Capture OpenMC output from standard out
    openmc_exec : str
        Path to OpenMC executable
    cwd : str, optional
        Path to working directory to run in. Defaults to the current working directory.

    """
    return _run([openmc_exec, '-p'], output, cwd)


def calculate_volumes(threads=None, output=True, cwd='.',
                      openmc_exec='openmc', mpi_args=None):
    """Run stochastic volume calculations in OpenMC.

    This function runs OpenMC in stochastic volume calculation mode. To specify
    the parameters of a volume calculation, one must first create a
    :class:`openmc.VolumeCalculation` instance and assign it to
    :attr:`openmc.Settings.volume_calculations`. For example:

    >>> vol = openmc.VolumeCalculation(domains=[cell1, cell2], samples=100000)
    >>> settings = openmc.Settings()
    >>> settings.volume_calculations = [vol]
    >>> settings.export_to_xml()
    >>> openmc.calculate_volumes()

    Parameters
    ----------
    threads : int, optional
        Number of OpenMP threads. If OpenMC is compiled with OpenMP threading
        enabled, the default is implementation-dependent but is usually equal to
        the number of hardware threads available (or a value set by the
        :envvar:`OMP_NUM_THREADS` environment variable).
    output : bool, optional
        Capture OpenMC output from standard out
    openmc_exec : str, optional
        Path to OpenMC executable. Defaults to 'openmc'.
    mpi_args : list of str, optional
        MPI execute command and any additional MPI arguments to pass,
        e.g. ['mpiexec', '-n', '8'].
    cwd : str, optional
        Path to working directory to run in. Defaults to the current working
        directory.

    See Also
    --------
    openmc.VolumeCalculation

    """
    args = [openmc_exec, '--volume']

    if isinstance(threads, Integral) and threads > 0:
        args += ['-s', str(threads)]
    if mpi_args is not None:
        args = mpi_args + args

    return _run(args, output, cwd)


def run(particles=None, threads=None, geometry_debug=False,
        restart_file=None, tracks=False, mpi_procs=1, output=True,
        openmc_exec='openmc', mpi_exec='mpiexec', cwd='.', ppn=1):
    """Run an OpenMC simulation.

    Parameters
    ----------
    particles : int, optional
        Number of particles to simulate per generation.
    threads : int, optional
        Number of OpenMP threads. If OpenMC is compiled with OpenMP threading
        enabled, the default is implementation-dependent but is usually equal to
        the number of hardware threads available (or a value set by the
        :envvar:`OMP_NUM_THREADS` environment variable).
    geometry_debug : bool, optional
        Turn on geometry debugging during simulation. Defaults to False.
    restart_file : str, optional
        Path to restart file to use
    tracks : bool, optional
        Write tracks for all particles. Defaults to False.
    output : bool
        Capture OpenMC output from standard out
    cwd : str, optional
        Path to working directory to run in. Defaults to the current working
        directory.
    openmc_exec : str, optional
        Path to OpenMC executable. Defaults to 'openmc'.
    mpi_exec : str, optional
        MPI execute command. Defaults to 'mpiexec'.
    cwd : str, optional
        Path to working directory to run in. Defaults to the current working directory.
    ppn : int, optional
        Processes per node.

    """

    post_args = ' '
    pre_args = ''

    if isinstance(particles, Integral) and particles > 0:
        post_args += '-n {0} '.format(particles)

    if isinstance(threads, Integral) and threads > 0:
        post_args += '-s {0} '.format(threads)

    if geometry_debug:
        post_args += '-g '

    if isinstance(restart_file, string_types):
        post_args += '-r {0} '.format(restart_file)

    if tracks:
        post_args += '-t'

    if isinstance(mpi_procs, Integral) and mpi_procs > 1:
        pre_args += '{} -n {} '.format(mpi_exec, mpi_procs)

    if isinstance(ppn, Integral) and ppn > 0:
        pre_args += '-ppn {0} '.format(ppn)

    command = pre_args + openmc_exec + ' ' + post_args

    return _run(command, output, cwd)
