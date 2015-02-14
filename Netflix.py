#!/usr/bin/env python3

# -------------------
# imports for RMSE.py
# -------------------

from functools import reduce
from numpy     import mean, sqrt, square, subtract
from sys       import version


def rmse_numpy (a, p) :
   return sqrt(mean(square(subtract(a, p))))

def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        movieID = s
        v    = netflix_eval(i, j)
        netflix_print(w, i, j, v)


