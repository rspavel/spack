# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Cogl(CMakePackage):
    """CoGL is a stand-alone meso-scale simulation code used to analyze pattern
    formation in ferroelastic materials using the Ginzburg–Landau approach. It
    models transitions from a face-centered cubic parent phase to a
    body-centered tetragonal product phase due to either a rapid decrease in
    temperature or an external deformation. By solving the force balance
    equations that use a nonlinear elastic free-energy functional and also
    incorporate inertial and viscous forces, the strains are computed at each
    point on a regular three-dimensional grid. The code allows the study of
    nucleation and growth of phase changes on loading-unloading and
    heating-cooling protocols as a function of strain rates."""

    homepage = "https://github.com/exmatex/CoGL"
    git = "https://github.com/exmatex/CoGL.git"
    url = "https://github.com/exmatex/CoGL/archive/master.zip"

    version('master',  branch='master')

    depends_on('gl')
    depends_on('cuda')
    depends_on('freeglut')