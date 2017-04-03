import csv

def readCSV(fileName):
    with open(fileName) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        dataAsList = map(tuple, datareader)
        return dataAsList

def writeToFile(fileName,celebrityNames):
	with open("celebritynames.csv", "w") as outfile:
		for name in celebrityNames:
			if not name:
				continue
			# names = name.split(' ')
			fb_likes, twitter_likes = celebrityNames[name]
			celebrityRow = [name,fb_likes,twitter_likes]
			wr = csv.writer(outfile, dialect='excel')
			wr.writerow(celebrityRow)

def writeToFileMovieRevenue(fileName,movieRevenues):
	with open("movieRevenue.csv", "w") as outfile:
		for movie in movieRevenues:
			if not movie:
				continue
			# names = name.split(' ')
			movieRow = [movie, movieRevenues[movie]]
			wr = csv.writer(outfile, dialect='excel')
			wr.writerow(movieRow)
