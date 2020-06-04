# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install multi-bgk
#
# You can edit this file again by typing:
#
#     spack edit multi-bgk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class MultiBgk(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/lanl/Multi-BGK"
    url      = "https://github.com/lanl/Multi-BGK/archive/master.tar.gz"
    git      = "https://github.com/lanl/Multi-BGK.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('develop', branch='master')

    # FIXME: Add dependencies if required.
    depends_on('mpi')

    @property
    def build_targets(self):
        targets = []
        targets.append('CC = {0}'.format(self.spec['mpi'].mpicc))
        targets.append('DIR= {0}'.format(self.stage.source_path + "/"))
        return targets

    def build(self, spec, prefix):
        buildDir = self.stage.source_path
        mkdirp(os.path.join(buildDir, "obj"))
        mkdirp(os.path.join(buildDir, "exec"))
        mkdirp(os.path.join(buildDir, "input"))
        mkdirp(os.path.join(buildDir, "Data"))
        make(*self.build_targets)

    def install(self, spec, prefix):
        install_tree('exec', prefix.exec)
        install_tree('input', prefix.input)
        install_tree('Data', prefix.Data)
