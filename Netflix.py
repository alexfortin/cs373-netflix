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
# Caches
userAverage = json.load(open('/u/afortin/downing/cs373/p2-netflix/netflix-tests/nrc523-ucache.json'))
meanFile = json.load(open('/u/afortin/downing/cs373/p2-netflix/netflix-tests/jab5948-movie-stats.json'))
actualFile = json.load(open('/u/afortin/downing/cs373/p2-netflix/netflix-tests/pma459-answersCache.json'))
dateFile = json.load(open('/u/afortin/downing/cs373/p2-netflix/cs373-netflix/data.json'))
userAverageYear = json.load(open('/u/afortin/downing/cs373/p2-netflix/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval.json'))

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

    w.write("RMSE: " + "%.2f" % rmse(predictedData, actualData) + "\n")
        
            
def netflix_write(movieID, customerRatings, w) :
    assert(len(movieID) > 0)

    w.write(movieID)
    for s in customerRatings :
        w.write("%.1f" % float(s) + "\n")


def predictRatings(movieID, customerList) :
    assert(len(movieID) > 0)
    global userAverage
    global meanFile
    global predictedData
    global dateFile
    global userAverageYear

    customerRating = []

    for s in customerList :
        rating = []
        movieYear = dateFile[movieID[:-2]]
        yearAverage = userAverageYear[s[:-1]]
        found = False
        for i in yearAverage :
            year = i[0].split('-')
            if (movieYear >= year[0] and movieYear <= year[1]) :
                rating.append(i[1])
                found = True
        rating.append(userAverage[s[:-1]]['average'])
        if(not found) :
            rating.append(meanFile[int(movieID[:-2])][0])
        predictedRating = mean(rating)
        customerRating.append(str(predictedRating))
        predictedData.append(predictedRating) 
    return customerRating    

def actualRating(movieID, customerList) :
    assert(len(movieID) > 0)
    assert(len(customerList) > 0)

    global actualData
    global actualFile

    for s in customerList :
        actualData.append(int(actualFile[movieID[:-2]][s[:-1]]))
