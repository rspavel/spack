# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RPermute(RPackage):
    """A set of restricted permutation designs for freely exchangeable, line
    transects (time series), and spatial grid designs plus permutation of
    blocks (groups of samples) is provided. 'permute' also allows split-plot
    designs, in which the whole-plots or split-plots or both can be
    freely-exchangeable or one of the restricted designs. The 'permute'
    package is modelled after the permutation schemes of 'Canoco 3.1'
    (and later) by Cajo ter Braak."""

    homepage = "https://github.com/gavinsimpson/permute"
    url      = "https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/permute"

    version('0.9-4', '569fc2442d72a1e3b7e2d456019674c9')

    depends_on('r@2.14:')
