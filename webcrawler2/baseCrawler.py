import abc

class BaseCrawler(abc.ABC):
    
    @abc.abstractmethod
    def crawl(self):
        # crawl the site and insert the the data gathered from in the database
        pass
