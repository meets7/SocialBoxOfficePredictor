
# coding: utf-8

# In[17]:

import numpy as np
import pandas as pd
# import scipy.stats as stats
import sklearn
import csv
import hashlib
import matplotlib.pyplot as plt

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
print dataset.columns
print len(dataset)


# In[18]:

from sklearn.model_selection import train_test_split
trainData, testData = train_test_split(dataset, test_size = 0.3)


# In[19]:

def getRevenueClass(budget,revenue):
    profit = int((revenue - budget)/float(budget))
    if profit == 0:
        return 0
    if profit == 1:
        return 1
    if profit == 2:
        return 2
    if profit == 3:
        return 3
    if profit >= 4:
        return 4
    return -1
        
    


# In[25]:

import statsmodels.formula.api as smf
lm = smf.ols(formula='Revenue ~ YT_Count+ YT_Dislike + IMDBVotes + Budget', data=trainData).fit()

preds = lm.predict(testData)
predictions = []

for value in preds:
    predictions.append(value)

counter = 0
correctCount = 0
percentErrorCorrectCount = 0
revenueList = testData['Revenue']
budgetList = testData['Budget'].tolist()
for realValue in revenueList:
    predictedValue = predictions[counter]
    budget = budgetList[counter]
    actualClass = getRevenueClass(budget,realValue)
    predictedClass = getRevenueClass(budget,predictedValue)
    if(actualClass == predictedClass):
        correctCount = correctCount + 1
    counter = counter + 1
    ###
    diff = abs(realValue - predictedValue)
    #     print diff
    percentError = diff/float(realValue)
        # print str(percentError) + ":" + str(diff)
    if percentError < 0.25:
        percentErrorCorrectCount = percentErrorCorrectCount + 1

print correctCount
print correctCount*100/float(698)
#print percentErrorCorrectCount*100/float(698)



