from AACResourceCrawler import AACResourceCrawler
from requestWrapper import RequestWrapper


data = RequestWrapper()

aac_crawler = AACResourceCrawler()
aac_crawler.crawl(data)
