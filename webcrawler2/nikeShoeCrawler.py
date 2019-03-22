import mechanicalsoup
import re
from baseCrawler import BaseCrawler
from emailClient import EmailClient
from clothingInfo import ClothingInfo

class NikeShowCrawler(BaseCrawler):
    def crawl(self):
        self.__badURL = []
        self.__browser = mechanicalsoup.StatefulBrowser()
        __link_regex = r'\<a href\=\"([\w\:\/]*www\.nike\.com\/ca\/t\/[\w\d\/\-]*)\"\>'
        self.__email_client = EmailClient()
        __siteurl = "https://store.nike.com/ca/en_gb/pw/mens-shoes/7puZoi3?intpromo=MLP-MEN%3ATOPNAV%3ASU18%3AMNSXCAT%3ASHOPMEN%3ASHOES&ipp=120"
   
        try:
            self.__browser.open(__siteurl)
            __htmlContents = str(self.__browser.get_current_page().findAll(True))

            __links_to_search = re.compile(__linkregex)
            self.__links = links_to_search.findall(__htmlContents)

            if len(links) == 0:
                __message = f'The link regex {__link_regex} did not come up with any values at the url {__siteurl}'
                self.__email_client.sendMessage(__message)

            __crawl_item_links()
        except:
            __message = f'exception raised when opening site: {__siteurl}'
            self.__email_client.sendMessage(__message)

            
    def __crawl_item_links(self):
        __price_regex = r'CAD" data-react-helmet="true" property="og:price:currency"/><meta content=\"([\d\.]+)'
        __item_regex = r'\-helmet\=\"true\" name\=\"description\"\/><meta content\=\"([^\"]*)'
        __image_regex = r'image\" data-react-helmet=\"true\" href=\"([^\"]*)'
        for link in self.__links:
            try:
                self.__browser.open(link)
                __htmlContents = str(browser.get_current_page().findAll(True))
                
                __nike_price = re.compile(__price_regex)
                __prices = __nike_price.findall(__htmlContents)

                __nike_item = re.compile(__item_regex)
                __items = __nike_item.findall(__htmlContents)

                __nike_image = re.compile(__image_regex)
                __images = __nike_image.findall(__htmlContents)

                if(len(__images) > 2 and len(__prices) > 0 and len(__items) > 0):
                    __clothing_info = ClothingInfo('nike', link, __items[0],  __prices[0], __images[2])
                    print(__clothing_info.to_string())
                    # databaseWrapper.insert(__clothing_info.format())
                else:
                    __clothing_info = ClothingInfo('nike', link, __items, __prices, __images)
                    #self.__badURL.append(__clothing_info.toJson())

            except:
                __clothing_info = ClothingInfo('nike', link)
                #self.__badURL.append(__clothing_info.toJson())
               