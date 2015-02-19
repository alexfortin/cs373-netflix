#!/usr/bin/env python3

# -------------------
# imports for RMSE.py
# -------------------

import json
from functools  import reduce
from math       import sqrt
# from numpy     import mean, sqrt, square, subtract
from sys        import version


predictedData = []
actualData = []
# Caches
userAverage = json.load(open('/u/mck782/netflix-tests/nrc523-ucache.json'))
meanFile = json.load(open('//u/mck782/netflix-tests/jab5948-movie-stats.json'))
actualFile = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json'))
dateFile = json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json'))
userAverageYear = json.load(open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval.json'))

def rmse(predictedData, actualData) :
    assert(hasattr(predictedData, "__iter__"))
    assert(hasattr(actualData, "__iter__"))

    # return sqrt(mean(square(subtract(predictedData, actualData))))
    z = zip(predictedData, actualData)
    v = sum((x - y) ** 2 for x, y in z)
    return sqrt(v / len(predictedData))

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
            assert(int(movieID[:-2]) > 0)
            customer = s[:-1]
            customerRating = predictRatings(movieID, customer)
            actualData.append(int(actualFile[movieID[:-2]][customer]))    
            netflix_write(customerRating, w)

    w.write("RMSE: " + "%.2f" % rmse(predictedData, actualData) + "\n")
        
            
def netflix_write(customerRating, w) :
    assert(int(customerRating) > -1)
    w.write("%.1f" % float(customerRating) + "\n")


def predictRatings(movieID, customer) :
    assert(int(movieID[:-2]) > 0)
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
    # loop through all the years in cache of a users ratings per year
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

def actualRating(movieID, customer) :
    assert(int(movieID[:-2]) > 0)
    global actualFile

    return int(actualFile[movieID[:-2]][customer[:-1]])
