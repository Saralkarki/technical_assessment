'''
Things to do:
Scrape 2019 articles from these two websites:
1. https://www.nsenergybusiness.com/power/

2. https://www.esi-africa.com/category/news/
-----------
High level problem solving:

1. Scrape the url from site
2. Scrape data from individual url

'''
import scrapy
from ..items import urlItem
from scrapy.loader import ItemLoader

class articleSpider(scrapy.Spider):
    name = 'articles'
    #defining the page number
    page_number = 2
    start_urls = ['https://www.nsenergybusiness.com/power/']
    
    def parse(self,response):
        # finding the div for all the articles
        featured_article = response.xpath("//article[@class='featured']/div[@id='mian-article']/div[@class='cell medium-7 txt-part']")
        article_div = response.xpath("//div[@id='mian-article']")
        for article in article_div:
            l_1 = ItemLoader(item = urlItem(), selector = article)
            l_1.add_xpath('url',".//div[@class='cell medium-3 text-right']/a/@href")
            yield l_1.load_item()
        for article in featured_article:
            yield{
                'url': article.xpath(".//h2[@class='h1']/a/@href").extract_first()
            }
                    
        next_page = 'https://www.nsenergybusiness.com/power/page/'+ str(articleSpider.page_number)+ '/'
        if articleSpider.page_number < 5:
            articleSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
            
            
   


        
