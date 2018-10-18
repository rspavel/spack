# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class HpctoolkitExternals(AutotoolsPackage):
    """HPCToolkit performance analysis tool has many prerequisites and
    HpctoolkitExternals package provides all these prerequisites."""

    homepage = "http://hpctoolkit.org"
    git      = "https://github.com/HPCToolkit/hpctoolkit-externals.git"

    version('master')
    version('2017.06', tag='release-2017.06')

    depends_on('binutils+libiberty')
    depends_on('libdwarf')
    depends_on('libelf')
    depends_on('libmonitor')
    depends_on('libunwind')
    depends_on('libxml2')
    depends_on('xerces-c')

    depends_on("cmake")

    patch('libiberty64.patch')

    build_directory = 'bld'

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

        options.append('CFLAGS={0}'.format(self.compiler.pic_flag))
        options.append('CXXFLAGS={0}'.format(self.compiler.pic_flag))

        return options
