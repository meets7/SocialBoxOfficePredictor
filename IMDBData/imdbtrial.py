from imdb import IMDb
import datetime
import utility
ia = IMDb()

def getLastThreeMovies(lastMovies):
	count = 0
	lastThreeMovies = []
	for movie in lastMovies:
		movieInfo = ia.get_movie(movie.movieID)
		year = movieInfo.get('year')
		if year is None:
			continue
		if  movieInfo['year'] < 2017:
			lastThreeMovies.append(str(movieInfo))
			count = count + 1
		if count == 3:
			return lastThreeMovies

	return lastThreeMovies

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
			if cast is None:
				continue

			for a in cast[:2]:
				name = a.get('name')
				if not name or name in actorMoviesMap:
					continue
				workedIn = ia.get_person(a.getID(), info=["filmography"])
				lastMovies = workedIn.get("actor")
				if lastMovies is None:
					continue
				# lastThreeMovies = getLastThreeMovies(lastMovies)
				if len(lastMovies) > 20:
					actorMoviesMap[name] = lastMovies[:20]
				else:
					actorMoviesMap[name] = lastMovies
		except:
			continue

	return actorMoviesMap


actorMap = ReadAllActors()
utility.writeToFile(actorMap)


# http://stackoverflow.com/questions/29710348/how-to-find-list-of-movies-acted-by-an-actor
