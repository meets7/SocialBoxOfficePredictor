import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Crawler
import sys
import utility

class FanPageListScrapper(scrapy.Spider):
	name = "celebrityPageScrapper"

	def start_requests(self):
		baseUrl = "http://fanpagelist.com/search.php?keyword="
		celebrityNames = utility.readCSV(sys.argv[1])[1:]
		urls = []
		for name in celebrityNames:
			celebrityUrl = baseUrl + name[0] + '+' + name[1]
			urls.append(celebrityUrl)

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		numList = response.css('.fb_stats::text').re(r'([0-9]+)')
		number = int(''.join(map(str,numList)))
		print "---------------------------------------------------------"
		print str(number)
		print "---------------------------------------------------------"

def main():
	if len(sys.argv) < 2:
		print "Specify file name"
		return

	process = CrawlerProcess({
	    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(FanPageListScrapper)
	process.start()

if __name__ == "__main__":
    main()