from nikeShoeCrawler import NikeShoeCrawler
from nikeClothesCrawler import NikeClothesCrawler
from ZapposClothesCrawl import ZapposClothesCrawler
from ZapposShoeCrawler import ZapposShoeCrawler
from requestWrapper import RequestWrapper


data = RequestWrapper()

nike_shoe_crawler = NikeShoeCrawler()
nike_shoe_crawler.crawl(data)

zappos_shoe_crawler = ZapposShoeCrawler()
zappos_shoe_crawler.crawl(data)

zappos_shorts_crawler = ZapposClothesCrawler()
zappos_shorts_crawler.crawl(data)



nike_clothes_crawler = NikeClothesCrawler()
nike_clothes_crawler.crawl(data)
