
# import the required libraries
import scrapy
from ..items import urlItem
from scrapy.loader import ItemLoader

#inherit from the scrapy.Spider class
class articleSpider(scrapy.Spider):
    name = 'urls'
    #defining the page number 
    page_number = 2
    start_urls = ['https://www.nsenergybusiness.com/power/']
    
    def parse(self,response):
        # url for the featured articles
        featured_article = response.xpath("//article[@class='featured']/div[@id='mian-article']/div[@class='cell medium-7 txt-part']")
        #url for other articles
        main_article = response.xpath("//div[@id='mian-article']")

        #loop through the main articles and scraping the url
        for article in main_article:
            l= ItemLoader(item = urlItem(), selector = article)
            l.add_xpath('url',".//div[@class='cell medium-3 text-right']/a/@href")
            yield l.load_item()
        #looping through the featured articles and scraping the url
        for article in featured_article:
            yield{
                'url': article.xpath(".//h2[@class='h1']/a/@href").extract_first()
            }
        # define the url for the next_page link          
        next_page = 'https://www.nsenergybusiness.com/power/page/'+ str(articleSpider.page_number)+ '/'
        # run loop until page 175 , and extract all urls for articles from 2019
        if articleSpider.page_number <=  175:
            articleSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
            
            
   


        
