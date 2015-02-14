#!/usr/bin/env python3

# -------------------
# imports for RMSE.py
# -------------------

from functools import reduce
from numpy     import mean, sqrt, square, subtract
from sys       import version


def rmse_numpy (a, p) :
   return sqrt(mean(square(subtract(a, p))))

