
class ClothingInfo:

    def __init__(self, website = None, item_link = None, item = None,  price = None, image_link = None):
        self.__website = website
        self.__item = item
        self.__item_link = item_link
        self.__price = price
        self.__image_link = image_link

    def set_website(self, website):
        self.__website = website

    def get_website(self):
        return self.__website

    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item
    
    def set_item_link(self, item_link):
        self.__item_link = item_link

    def get_item_link(self):
        return self.__item_link
    
    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_image_link(self, image_link):
        self.__image_link = image_link

    def get_image_link(self):
        return self.__image_link

    def to_string(self):
        return f"Website: {self.__website}, Item: {self.__item}, Item link: {self.__image_link}, Price: {self.__price}, Image link: {self.__image_link}"