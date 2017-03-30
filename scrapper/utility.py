import csv

def readCSV(fileName):
    with open(fileName) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        dataAsList = map(tuple, datareader)
        return dataAsList