import scrapy
import csv
from ..items import ArticleItems

url_list = []
# import csv file with the urls from the NS ENERGY website
with open('urls_nsenergy.csv') as csv_file:
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
    name = 'ns_articles'
    start_urls = ['https://www.nsenergybusiness.com/features/oil-companies-investing-in-renewables-2019/']
    
    def parse(self,response):
        links = flat_list
        for link in links:
            yield scrapy.Request(link,self.parse_article)
            
    def parse_article(self, response):       
        items = ArticleItems()
        
        article_title = response.css('h1::text').extract()
        article_date = response.css("#date::text").extract()
        article_body = response.xpath("//div[@class='td-post-content']/p/text()").extract()
        article_body = ''.join(article_body)       
        image_link = response.xpath("//div[@class='cell small-12 medium-12 large-10']/img/@src").extract()
        category_1 = response.xpath("//p[@class='tags']/span[1]/a/text()").extract()
        category_2 = response.xpath("//p[@class='tags']/span[2]/a/text()").extract()
        category_3 = response.xpath("//p[@class='tags']/span[3]/a/text()").extract()

#     # Get the list of URLs, for example:
        items['article_title'] = article_title
        items['article_date'] = article_date
        items['article_body'] = article_body
        items['image_link'] = image_link

        yield items
        
   