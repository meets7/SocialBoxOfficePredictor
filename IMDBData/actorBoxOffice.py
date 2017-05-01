import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Crawler
import sys
import utility
import re
import urllib

class MovieBoxOfficeNumbersScrapper(scrapy.Spider):
	name = "boxOfficeSCrapper"
	custom_settings = {'COOKIES_ENABLED': 'false'}
	movieNames = {}
	movieActor = {}

	def readNames(self):
		movieData = utility.readCSV("data/last3Movies.csv")
		for movie in movieData:
			if len(movie) < 3:
				continue
			year = movie[2]
			if not year or int(year) >= 2017:
				continue
			movieName = movie[1]
			self.movieNames[movieName] = 0
			actor = movie[0]
			if actor in self.movieActor:
				self.movieActor[actor].append(movieName)
			else:
				self.movieActor[actor] = [movieName]

	def start_requests(self):
		baseUrl = "http://www.the-numbers.com/search?searchterm="
		self.readNames()
		urls = []
		for movie in self.movieNames:
			if not movie:
				continue
			keyword = urllib.quote_plus(movie)
			movieUrl = baseUrl + keyword
			urls.append(str(movieUrl))

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		try:
			boxOfficeRevenue = float(response.css('.data::text')[-1].extract().encode().replace('$','').replace(',',''))
		except:
			return
		movieName = re.search(r"(?<=term=)[a-zA-Z.:+]+",urllib.unquote(response.url)).group(0).replace('+',' ')
		self.movieNames[movieName] = boxOfficeRevenue


	def __str__(self):
	    return ""

def getAverage(revenue, actormovie):
	actorAverage = {}
	for actor in actormovie:
		sum = 0
		for movie in actormovie[actor]:
			sum = sum + revenue[movie]
		actorAverage[actor] = int(sum/len(actormovie[actor]))

	return actorAverage

def main():
	# if len(sys.argv) < 2:
	# 	print "Specify file name"
	# 	return

	process = CrawlerProcess({
	    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(MovieBoxOfficeNumbersScrapper)
	process.start()

	averageRevenue = getAverage(MovieBoxOfficeNumbersScrapper.movieNames, MovieBoxOfficeNumbersScrapper.movieActor)
	utility.writeToFileMovieRevenue(averageRevenue)
	# utility.writeToFile("celebrityNames.csv",FanPageListScrapper.celebrityNames)

if __name__ == "__main__":
    main()