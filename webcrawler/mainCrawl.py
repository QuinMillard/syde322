from nikeShoeCrawler import NikeShoeCrawler
from nikeClothesCrawler import NikeClothesCrawler
from ZapposClothesCrawl import ZapposClothesCrawler
from ZapposShoeCrawler import ZapposShoeCrawler
from requestWrapper import RequestWrapper

from emailClient import EmailClient

email_client = EmailClient()
siteurl = 'https://store.nike.com/ca/en_gb/pw/mens-clothing/1mdZ7pu?intpromo=MLP-MEN%3ATOPNAV%3ASU18%3AMNSXCAT%3ASHOPMEN%3ACLOTHING&ipp=120'
   
m = 'Exception raised when opening site - {}'.format(siteurl)


email_client.sendMessage(m)




# data = RequestWrapper()

# # nike_shoe_crawler = NikeShoeCrawler()
# # nike_shoe_crawler.crawl(data)

# zappos_shoe_crawler = ZapposShoeCrawler()
# zappos_shoe_crawler.crawl(data)

# zappos_shorts_crawler = ZapposClothesCrawler()
# zappos_shorts_crawler.crawl(data)



# nike_clothes_crawler = NikeClothesCrawler()
# nike_clothes_crawler.crawl(data)
