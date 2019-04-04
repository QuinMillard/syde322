import mechanicalsoup
import re
from baseCrawler import BaseCrawler
from emailClient import EmailClient
from clothingInfo import ClothingInfo

class NikeShoeCrawler(BaseCrawler):
    def crawl(self,request_wrapper):
        self.__bad_URL = []
        self.__browser = mechanicalsoup.StatefulBrowser()
        __link_regex = r'\<a href\=\"([\w\:\/]*www\.nike\.com\/ca\/t\/[\w\d\/\-]*)\"\>'
        self.__email_client = EmailClient()
        __siteurl = "https://store.nike.com/ca/en_gb/pw/mens-shoes/7puZoi3?intpromo=MLP-MEN%3ATOPNAV%3ASU18%3AMNSXCAT%3ASHOPMEN%3ASHOES&ipp=120"
   
       
        if(str(self.__browser.open(__siteurl)) == "<Response [200]>"):
            __htmlContents = str(self.__browser.get_current_page().findAll(True))

            __links_to_search = re.compile(__link_regex)
            self.__links = set(__links_to_search.findall(__htmlContents))
            
            if len(self.__links) == 0:
                __message = f"The link regex {__link_regex} did not come up with any values at the url {__siteurl}"
                print(__message)
                self.__email_client.sendErrorMessage(__message)
            self.__crawl_item_links(request_wrapper)
        else:
            __message = f"exception raised when opening site: {__siteurl}"
            print(__message)
            self.__email_client.sendErrorMessage(__message)

        if len(self.__bad_URL) > 0:
            __bad_URL_string = self.get_string_from_list(self.__bad_URL)
            __message = f"exception raised in the following items: {__bad_URL_string}"
            self.__email_client.sendErrorMessage(__message)

            
    def __crawl_item_links(self,request_wrapper):
        __price_regex = r'CAD" data-react-helmet="true" property="og:price:currency"/><meta content=\"([\d\.]+)'
        __item_regex = r'\-helmet\=\"true\" name\=\"description\"\/><meta content\=\"([^\"]*)'
        __image_regex = r'image\" data-react-helmet=\"true\" href=\"([^\"]*)'
        print(len(self.__links))
        for link in self.__links:
            if(str(self.__browser.open(link)) == "<Response [200]>"):
                __htmlContents = str(self.__browser.get_current_page().findAll(True))
                
                __nike_price = re.compile(__price_regex)
                __prices = __nike_price.findall(__htmlContents)

                __nike_item = re.compile(__item_regex)
                __items = __nike_item.findall(__htmlContents)

                __nike_image = re.compile(__image_regex)
                __images = __nike_image.findall(__htmlContents)

                if(len(__images) > 2 and len(__prices) > 0 and len(__items) > 0):
                    __clothing_info = ClothingInfo('Nike', link, __items[0],  __prices[0], __images[2])
                    print(__clothing_info.to_string())
                    response = request_wrapper.insert_into_db(__clothing_info.to_object())
                    print(response)    
                else:
                    __clothing_info = ClothingInfo('Nike', link, __items, __prices, __images)
                    self.__bad_URL.append(__clothing_info.to_string())
            else:
                __clothing_info = ClothingInfo('Nike', link)
                self.__bad_URL.append(__clothing_info.to_string())
    
    def get_string_from_list(self, list):
        __return_string = ""
        for item in list:
            __return_string = __return_string + item
        return __return_string
                