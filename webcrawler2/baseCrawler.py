from abc import ABC, abstractclassmethod

class BaseCrawler(ABC):
    
    @abstractclassmethod
    def crawl(self):
        # crawl the site and insert the the data gathered from in the database
        pass
