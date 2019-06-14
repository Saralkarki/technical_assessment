import scrapy
import csv
from ..items import ArticleItems

url_list = []
with open('url_data.csv') as csv_file:
    csvReader = csv.reader(csv_file)
    for row in csvReader:
        if row == ['url'] or row == ['']:
            pass
        else:
            url_list.append(row)
flat_list = []
for sublist in url_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)
class dataSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.nsenergybusiness.com/features/oil-companies-investing-in-renewables-2019/']
    
    def parse(self,response):
        links = flat_list
        for link in links:
            yield scrapy.Request(link,self.parse_article)
            
    def parse_article(self, response):       
        items = ArticleItems()
        
        article_title = response.css('h1::text').extract()
        article_date = response.css("#date::text").extract()
        article_body = response.xpath("//div[@class='cell small-12 medium-12 large-10']/p/text()").extract()
        article_body = ''.join(article_body)
        # image_link = response.css('.tile:nth-child(3) img , .size-full , .img_caption').attr('::src').extract()

#     # Get the list of URLs, for example:
        items['article_title'] = article_title
        items['article_date'] = article_date
        items['article_body'] = article_body
        # items['image_link'] = image_link

        yield items
        
   