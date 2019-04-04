import mechanicalsoup
import re
from baseCrawler import BaseCrawler
from emailClient import EmailClient
from clothingInfo import ClothingInfo

class ZapposClothesCrawler(BaseCrawler):
    def crawl(self,request_wrapper):
        self.__bad_URL = []
        self.__browser = mechanicalsoup.StatefulBrowser()
        __link_regex = r'(\/p\/nike[\w\d\/\-]*)'
        self.__email_client = EmailClient()
        __siteurl = "https://www.zappos.com/nike-shorts"
        __page = 1
        while True:
            if(str(self.__browser.open(__siteurl)) == "<Response [200]>"):
                __htmlContents = str(self.__browser.get_current_page().findAll(True))
                # print(__htmlContents)
                __links_to_search = re.compile(__link_regex)
                self.__links = set(__links_to_search.findall(__htmlContents))
                self.__links = ["https://www.zappos.com{0}".format(link) for link in self.__links]
                
                if len(self.__links) == 0 and __page == 1:
                    __message = f'The link regex {__link_regex} did not come up with any values at the url {__siteurl}'
                    print(__message)
                    self.__email_client.sendErrorMessage(__message)
                elif len(self.__links) == 0:
                    break

                self.__crawl_item_links(request_wrapper)

                __siteurl = f"https://www.zappos.com/nike-shorts/.zso?t=nike%20shorts&p={__page}"
                __page = __page + 1

            else:
                __message = f'exception raised when opening site: {__siteurl}'
                print(__message)
                self.__email_client.sendErrorMessage(__message)

            if len(self.__bad_URL) > 0:
                __bad_URL_string = self.__get_string_from_list(self.__bad_URL)
                __message = f'exception raised in the following items: {__bad_URL_string}'
                self.__email_client.sendErrorMessage(__message)

            
    def __crawl_item_links(self,request_wrapper):
        __price_regex = r'span class=\"_1q0kwWbBMG.*\">(\$\d\d\.\d\d)'
        __image_regex = r'\"(https:\/\/m\.media\-amazon\.com\/images[\w\d\/\-\.]*)\"\/><\/button>\,\s<img\salt\=\"MAIN\"'
        print(len(self.__links), ' number of items found')
        for link in self.__links:
            if(str(self.__browser.open(link)) == "<Response [200]>"):
                __htmlContents = str(self.__browser.get_current_page().findAll(True))
                
                __nike_price = re.compile(__price_regex)
                __prices = __nike_price.findall(__htmlContents)
        
                __item = link.split('/')[4].replace('-',' ')
                __endIndex = max(__item.find('short') + 5,__item.find('shorts') + 6)
                if __item.find('short') != -1 or __item.find('shorts') != -1 :
                    __item = __item[:__endIndex]

                __nike_image = re.compile(__image_regex)
                __images = __nike_image.findall(__htmlContents)

                if(len(__images) > 0 and len(__prices) > 0):
                    __clothing_info = ClothingInfo('Zappos', link, __item,  __prices[0][1:], __images[0])
                    print(__clothing_info.to_string())
                    response = request_wrapper.insert_into_db(__clothing_info.to_object())
                    print(response)      
                else:
                    __clothing_info = ClothingInfo('Zappos', link, __item, __prices, __images)
                    self.__bad_URL.append(__clothing_info.to_string())
            else:
                __clothing_info = ClothingInfo('Zappos', link)
                self.__bad_URL.append(__clothing_info.to_string())
    
    def __get_string_from_list(self, list):
        __return_string = ""
        for item in list:
            __return_string = __return_string + item
        return __return_string
                