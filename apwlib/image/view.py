# -*- coding: utf-8 -*-

""" apwlib
    ------
    
    Copyright (C) 2012 Adrian Price-Whelan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

################################################################################
# view.py
#

"""
TODO:
"""

__author__ = 'Adrian Price-Whelan <adrn@astro.columbia.edu>'
#__all__ = ["Angle", "RA", "Dec", "RADec"]

# Standard library dependencies (e.g. sys, os)
import math
import copy

# Third-party 
import matplotlib.pyplot as plt
import numpy as np

# Project Dependencies
import convert
import astrodatetime
from custom_errors import *
import globals