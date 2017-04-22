import csv

def writeToFile(actorMovieList):
	with open("last3Movies.csv", "w") as outfile:
		for actor in actorMovieList:
			if not actor:
				continue
			# names = name.split(' ')
			# movieList = ",".join(actorMovieList[actor])
			for m in actorMovieList[actor]:
				actorRow = [actor, m]
				wr = csv.writer(outfile, dialect='excel')
				wr.writerow(actorRow)

def readCSV(fileName):
    with open(fileName) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        dataAsList = map(tuple, datareader)
        return dataAsList