#
# Copyright (c) 2013 Christopher L. Felton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup,find_packages

setup(name = "fixed_point",
      version = "0.1dev",
      description = "Fixed-point object for MyHDL and DSP simulation",      
      license = "LGPL",
      platforms = ["Any"],
      author = "Christopher L. Felton",
      author_email = "cfelton@ieee.org",
      url = "https://bitbucket.org/cfelton/fixed_point",
      keywords = "HDL Fixed-Point Fixed Floating FPGA ASIC",

      packages = find_packages(),
      install_requires = ['myhdl>=0.10'],
      test_suite = 'nose.collector',
      tests_require = 'nose'
      )

