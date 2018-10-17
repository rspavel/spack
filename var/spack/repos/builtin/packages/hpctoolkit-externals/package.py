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


class HpctoolkitExternals(AutotoolsPackage):
    """HPCToolkit performance analysis tool has many prerequisites and
    HpctoolkitExternals package provides all these prerequisites."""

    homepage = "http://hpctoolkit.org"
    git      = "https://github.com/HPCToolkit/hpctoolkit-externals.git"

    version('master')
    version('2017.06', tag='release-2017.06')

    depends_on('binutils')
    depends_on('libdwarf')
    depends_on('libelf')
    depends_on('libmonitor')
    depends_on('libunwind')
    depends_on('libxml2')
    depends_on('xerces-c')

    depends_on("cmake")

    def configure_args(self):
        spec = self.spec

        options = []
        options.append('CC={0}'.format(spack_cc))
        options.append('CXX={0}'.format(spack_cxx))
        options.append('--with-binutils={0}'.format(spec['binutils'].prefix))
        options.append('--with-libdwarf={0}'.format(spec['libdwarf'].prefix))
        options.append('--with-libelf={0}'.format(spec['libelf'].prefix))
        options.append('--with-libmonitor={0}'.format(spec['libmonitor'].prefix))
        options.append('--with-libunwind={0}'.format(spec['libunwind'].prefix))
        options.append('--with-libxml2={0}'.format(spec['libxml2'].prefix))
        options.append('--with-xerces={0}'.format(spec['xerces-c'].prefix))

        return options
