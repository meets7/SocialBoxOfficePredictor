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

	def readNames(self):
		movieData = utility.readCSV(sys.argv[1])[1:]
		for movie in movieData:
			movieName = movie[11].decode('utf8').replace(u'\xa0', u'').encode('utf8')
			self.movieNames[movieName] = 0

	def getCelebrityName(self,url):
		pattern = r"(?<=keyword=)([a-zA-Z+]+)"
		keyword = re.search(pattern,url)
		name = keyword.group().replace('+',' ')
		return name

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
		boxOfficeRevenue = float(response.css('.data::text')[-1].extract().encode().replace('$','').replace(',',''))
		movieName = re.search(r"(?<=term=)[a-zA-Z.:+]+",urllib.unquote(response.url)).group(0).replace('+',' ')
		self.movieNames[movieName] = boxOfficeRevenue



	def __str__(self):
	    return ""

def main():
	if len(sys.argv) < 2:
		print "Specify file name"
		return

	process = CrawlerProcess({
	    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(MovieBoxOfficeNumbersScrapper)
	process.start()

	utility.writeToFileMovieRevenue("",MovieBoxOfficeNumbersScrapper.movieNames)
	# utility.writeToFile("celebrityNames.csv",FanPageListScrapper.celebrityNames)

if __name__ == "__main__":
    main()