import csv

def writeToFile(actorMovieList):
	with open("data/last3Movies.csv", "w") as outfile:
		for actor in actorMovieList:
			if not actor:
				continue
			# names = name.split(' ')
			# movieList = ",".join(actorMovieList[actor])
			for m in actorMovieList[actor]:
				movieName = ""
				try:
					movieName = m.get('title')
					# movieName = movieName.encode('utf-8').strip()
				except:
					continue
				if not movieName:
					continue
				actorRow = [actor, movieName]
				wr = csv.writer(outfile, dialect='excel')
				try:
					wr.writerow(actorRow)
				except:
					continue

def readCSV(fileName):
    with open(fileName) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        dataAsList = map(tuple, datareader)
        return dataAsList

def writeToFileMovieRevenue(averageRevenues):
	with open("data/actorRevenue.csv", "w") as outfile:
		for actor in averageRevenues:
			if not actor:
				continue
			# names = name.split(' ')
			actorRow = [actor, averageRevenues[actor]]
			wr = csv.writer(outfile, dialect='excel')
			wr.writerow(actorRow)