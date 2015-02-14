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
    _list = []
    movieID = ""
    for s in r :
        if ':' in s:
            # do some work
            if movieID == "" :
                movieID = s
            else :
                # process movieID with _list
                # set movieID to s
                netflix_write(movieID, _list, w)
        else :
            _list.append(s)
            
        
            
def netflix_write(movieID, customers, w) :
    w.write(movieID)
    for s in customers :
        w.write(s)


