import scrapy
import csv
from ..items import ArticleItems

url_list = []
# import csv file with the urls from the NS ENERGY website
with open('url_esi.csv') as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        #delete empty rows 
        if row == ['url'] or row == ['']:
            pass
        else:
            url_list.append(row)
#flatten out the list of url to array so that they can be used to parse by scrapy
flat_list = []
for sublist in url_list:
    for item in sublist:
        flat_list.append(item)

#Spider class 
class dataSpider(scrapy.Spider):
    name = 'es_af_articles'
    start_urls = ['https://www.esi-africa.com/industry-sectors/generation/closure-of-fiddlers-ferry-coal-fired-power-station-on-the-cards/']
    
    def parse(self,response):
        links = flat_list
        for link in links:
            yield scrapy.Request(link,self.parse_article)
            
    def parse_article(self, response):       
        items = ArticleItems()
        
        article_title = response.css('.entry-title::text').extract()
        article_date = response.css(".td-post-title .td-module-date::text").extract()
        article_body = response.css("p,strong").css('::text').extract()
        article_body = ''.join(article_body)       
        image_link = response.xpath("//div[@class='td-post-featured-image']/figure/a/@href").extract()

#     # Get the list of URLs, for example:
        items['article_title'] = article_title
        items['article_date'] = article_date
        items['article_body'] = article_body
        items['image_link'] = image_link
        yield items
        
   