import csv

def readCSV(fileName):
    with open(fileName) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        dataAsList = map(tuple, datareader)
        return dataAsList

movieData = readCSV("FinalDataSet.csv")[2443:]
predictions = readCSV("output.csv")

correct = 0
count = 0
for m in movieData:
	actual = float(m[9])
	predicted = float(predictions[count][0])
	diff = abs(actual - predicted)
	percentError = diff/actual
	if percentError < 0.25:
		correct = correct + 1

	count = count + 1 

print correct/float(count-1)
