
import numpy as np
import pandas as pd
import sklearn
import csv
import hashlib
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

from sklearn.model_selection import train_test_split

def convertMovieName(ttid):
	return ttid[2:]

def convertPGRating(rating):
	#g, pg, pg-13, r, nc-17
	# rating = rating.lower()
	ratingDict = {
	    'P': 1,
	    'PG': 2,
	    'PG-13': 3,
	    'R': 4,
	    'NC-17': 5,
	}
	if rating not in ratingDict:
		return 0
	return ratingDict[str(rating).strip()]


converterFunctions = {}
converterFunctions[12] = convertPGRating
converterFunctions[1] = convertMovieName

dataset = pd.read_csv("data/FinalDataSet.csv", delimiter=",",usecols = [1,2,3,4,5,6,7,8,9,10,11,12], converters=converterFunctions)

trainData, testData = train_test_split(dataset, test_size = 0.2)


lm = smf.ols(formula='Revenue ~ Budget+YT_Count + Rated + IMDBVotes', data=trainData).fit_regularized()

preds = lm.predict(testData)
predictions = []
correctCount = 0
for value in preds:
    predictions.append(value)

# All time blockbluster = 4x
# BlockBuster = 3x
# Super Hit = 2.5x
# Hit = 2x
# Averge = 1.5x
# Else Flop
# buckets = {4:,

counter = 0
for a in testData['Revenue,Budget']:
    realValue = a
    predictedValue = predictions[counter]
    counter = counter + 1
    diff = abs(realValue - predictedValue)
    percentError = diff/float(realValue)
    if percentError < 0.35:
        correctCount = correctCount + 1

print correctCount
print correctCount*100/float(len(testData))


