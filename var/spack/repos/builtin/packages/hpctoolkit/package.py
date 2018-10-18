##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os


class Hpctoolkit(AutotoolsPackage):
    """HPCToolkit is an integrated suite of tools for measurement and analysis
    of program performance on computers ranging from multicore desktop systems
    to the nation's largest supercomputers. By using statistical sampling of
    timers and hardware performance counters, HPCToolkit collects accurate
    measurements of a program's work, resource consumption, and inefficiency
    and attributes them to the full calling context in which they occur."""

    homepage = "http://hpctoolkit.org"
    git      = "https://github.com/HPCToolkit/hpctoolkit.git"

    version('master')
    version('2017.06', tag='release-2017.06')

    variant('mpi', default=True, description='Enable MPI supoort')
    variant('papi', default=True, description='Enable PAPI counter support')

    depends_on('papi', when='+papi')
    depends_on('mpi', when='+mpi')
    depends_on('hpctoolkit-externals@2017.06', when='@2017.06')
    depends_on('hpctoolkit-externals@master', when='@master')

    # Doesn't actually need to autoreconf
    depends_on('autoconf')
    depends_on('automake')
    depends_on('libtool')

    def configure_args(self):
        spec = self.spec

        options = []
        options.append('CC={0}'.format(spack_cc))
        options.append('CXX={0}'.format(spack_cxx))
        options.append('--with-externals={0}'.format(spec['hpctoolkit-externals'].prefix))
        if '+mpi' in spec:
            options.append(['MPICXX=%s' % spec['mpi'].mpicxx])
        if '+papi' in spec:
            options.append(['--with-papi=%s' % spec['papi'].prefix])

        return options
