#!/usr/bin/env python3

# -------------------
# imports for RMSE.py
# -------------------

from functools import reduce
from numpy     import mean, sqrt, square, subtract
from sys       import version
import json

predictedData = []
actualData = []

def rmse(predictedData, actualData) :
    assert(hasattr(predictedData, "__iter__"))
    assert(hasattr(actualData, "__iter__"))

    return sqrt(mean(square(subtract(predictedData, actualData))))

def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """
    global actualData
    global predictedData

    # w.write(str(rmse(predictedData, actualData)))

    customerList = []
    movieID = ""
    for s in r :
        if ':' in s:
            assert(':' in s)

            if movieID == "" :
                movieID = s
            else :
                assert(len(movieID) > 0)
                
                customerRating = predictRatings(movieID, customerList)
                actualRating(movieID, customerList)
                netflix_write(movieID, customerRating, w)
                del customerList [:]
                movieID = s
        else :
            customerList.append(s)
    customerRating = predictRatings(movieID, customerList)
    actualRating(movieID, customerList)
    netflix_write(movieID, customerRating, w)

    w.write(str(rmse(predictedData, actualData)) + "\n")
        
            
def netflix_write(movieID, customerRatings, w) :
    assert(len(movieID) > 0)

    w.write(movieID)
    for s in customerRatings :
        w.write(s + "\n")


def predictRatings(movieID, customerList) :
    assert(len(movieID) > 0)

    customerRating = []
    global predictedData
    for s in customerList :
        customerRating.append("3.7")
        predictedData.append(3.7) 
    return customerRating    

def actualRating(movieID, customerList) :
    assert(len(movieID) > 0)
    assert(len(customerList) > 0)

    global actualData
    actualFile = json.load(open('/u/afortin/downing/cs373/p2-netflix/netflix-tests/pma459-answersCache.json'))
    for s in customerList :
        actualData.append(int(actualFile[movieID[:-2]][s[:-1]]))
