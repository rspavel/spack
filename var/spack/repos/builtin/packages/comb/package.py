# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Comb(CMakePackage):
    """Comb is a communication performance benchmarking tool. It is used to
    determine performance tradeoffs in implementing communication patterns
    on high performance computing (HPC) platforms. At its core comb runs
    combinations of communication patterns with execution patterns, and
    memory spaces in order to find efficient combinations."""

    homepage = "https://github.com/LLNL/Comb"
    git = "https://github.com/LLNL/Comb.git"
    url = "https://github.com/LLNL/Comb/archive/v0.1.1.zip"

    version('develop',  branch='develop', submodules='True')
    version('master',  branch='master', submodules='True')
    version('0.1.1', sha256='427ffdcce9f56825b9bf392729573d5d5ee9413312f8114e548340d5b7b4e38e')
    version('0.1.0', sha256='9e4f5ed8ae3c225158ff7370e9f87426a09587e2efaff54c9ea51c9ac8e71afd')

    variant('mpi', default=True, description="Enable MPI Support")
    variant('cuda', default=False, description="Enable Cuda Support")

    depends_on('cuda', when='+cuda')
    depends_on('mpi', when='+mpi')
