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
    # looping through every line of input
    for s in r :
        # colon signifies movie ID
        if ':' in s:
            assert(':' in s)

            movieID = s
            w.write(movieID)
        else :
            assert(len(movieID) > 0)
            customer = s[:-1]
            customerRating = predictRatings(movieID, customer)
            actualData.append(int(actualFile[movieID[:-2]][customer]))    
            netflix_write(movieID, customerRating, w)

    w.write("RMSE: " + "%.2f" % rmse(predictedData, actualData) + "\n")
        
            
def netflix_write(movieID, customer, w) :
    assert(len(movieID) > 0)

    w.write("%.1f" % float(customer) + "\n")


def predictRatings(movieID, customer) :
    assert(len(movieID) > 0)
    global userAverage
    global meanFile
    global predictedData
    global dateFile
    global userAverageYear

    rating = []
    movieYear = dateFile[movieID[:-2]]
    yearAverage = userAverageYear[customer]
    customerRating = ""
    found = False
    for i in yearAverage :
        year = i[0].split('-')
        if (movieYear >= year[0] and movieYear <= year[1]) :
            customerRating = i[1]
            found = True
    if(not found) :
        customerRating = userAverage[customer]['average']
    meanRating = meanFile[int(movieID[:-2])][0]
    predictedRating = (customerRating + meanRating) / 2
    predictedData.append(predictedRating) 
    return predictedRating                                                                                                                       

def actualRating(movieID, customerList) :
    assert(len(movieID) > 0)
    assert(len(customerList) > 0)

    global actualData
    global actualFile

    for s in customerList :
        actualData.append(int(actualFile[movieID[:-2]][s[:-1]]))
