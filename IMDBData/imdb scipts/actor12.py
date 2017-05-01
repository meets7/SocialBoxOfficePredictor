from imdb import IMDb
import datetime
import utility
ia = IMDb()

def ReadAllActors():
	movies = utility.readCSV("data/MovieDetail.csv")
	actorMoviesMap = {}
	count = 1
	for movie in movies[1:]:
		try:
			if count % 20 == 0:
				print count
				print datetime.datetime.now()
			count = count + 1
			movieId = movie[1][2:]
			if not movieId or len(movieId) != 7:
				continue
			movieInfo = ia.get_movie(movieId)
			cast = movieInfo.get('cast')
			movieName = movieInfo.get('title')
			if cast is None or movieName is None:
				continue

			for a in cast[:5]:
				try:
					name = str(a.get('name'))
				except:
					continue
				if not name:
					continue
				if movieName in actorMoviesMap and len(actorMoviesMap[movieName]) < 2:
					actorMoviesMap[movieName].append(name)
				else:
					actorMoviesMap[movieName] = [name]
		except:
			continue

	return actorMoviesMap


actorMap = ReadAllActors()
utility.writeToFileMovieActors(actorMap)


# http://stackoverflow.com/questions/29710348/how-to-find-list-of-movies-acted-by-an-actor
