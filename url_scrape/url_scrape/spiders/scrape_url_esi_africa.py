import scrapy
from ..items import urlItem
from scrapy.loader import ItemLoader

#inherit from the scrapy.Spider class
class articleSpider(scrapy.Spider):
    name = 'urlesi'
    #defining the page number 
    page_number = 2
    start_urls = ['https://www.esi-africa.com/category/news/']
    
    def parse(self,response):
        #url for  articles
        article_links = response.xpath("//div[@class='td-item-details td-category-small']")
        for link in article_links:
            yield {
                'url': link.xpath(".//h3[@class='entry-title td-module-title']/a/@href").extract_first()               
            }    

        # define the url for the next_page link      
        next_page = 'https://www.esi-africa.com/category/news/page/'+str(articleSpider.page_number)+'/'    
        # run loop until page 52 , and extract all urls for articles from 2019
        if articleSpider.page_number <  52:
            articleSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)

       
       
   


        
