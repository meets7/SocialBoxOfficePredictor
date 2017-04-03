import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Crawler
import sys
import utility
import re

class FanPageListScrapper(scrapy.Spider):
	name = "celebrityPageScrapper"
	custom_settings = {'COOKIES_ENABLED': 'false'}
	celebrityNames = {}

	def readNames(self):
		movieData = utility.readCSV(sys.argv[1])[1:]
		for movie in movieData:
			self.celebrityNames[movie[1]] = (-1,-1)
			self.celebrityNames[movie[6]] = (-1,-1)
			self.celebrityNames[movie[10]] = (-1,-1)
			self.celebrityNames[movie[14]] = (-1,-1)

	def getCelebrityName(self,url):
		pattern = r"(?<=keyword=)([a-zA-Z+]+)"
		keyword = re.search(pattern,url)
		name = keyword.group().replace('+',' ')
		return name

	def start_requests(self):
		baseUrl = "http://fanpagelist.com/search.php?keyword="
		self.readNames()
		urls = []
		for name in self.celebrityNames:
			if not name:
				continue 
			names = name.split(' ')
			keyword = ''
			for n in names:
				if not keyword:
					keyword = n
					continue
				keyword = keyword + '+' + n
			celebrityUrl = baseUrl + keyword
			urls.append(celebrityUrl)

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		fbnumList = response.css('.fb_stats::text').re(r'([0-9]+)')
		twitternumList = response.css('.twitter_stats::text').re(r'([0-9]+)')
		if fbnumList:
			fbnumber = int(''.join(map(str,fbnumList)))
		else:
			fbnumber = 0
		if twitternumList:
			twitternumber = int(''.join(map(str,twitternumList)))
		else:
			twitternumber = 0
		name = self.getCelebrityName(response.url)
		self.celebrityNames[name] = (fbnumber,twitternumber)
		# utility.writeToFile("celebrityNames.csv",name,fbnumber,twitternumber)


	def __str__(self):
	    return ""

def main():
	if len(sys.argv) < 2:
		print "Specify file name"
		return

	process = CrawlerProcess({
	    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(FanPageListScrapper)
	process.start()

	utility.writeToFile("celebrityNames.csv",FanPageListScrapper.celebrityNames)

if __name__ == "__main__":
    main()