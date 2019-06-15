import scrapy
import csv
# from ..items import ArticleItems

# Import the urls
links = csv.reader('urls_nsenergy.csv')
#convert the links to array
links = []
for link in links:
    links.append(link)
print(links)

# class dataSpider(scrapy.Spider):
#     name = 'articles_ns'
#     page_number = 2
#     start_urls = [
#         'https://www.nsenergybusiness.com/power/'
#     ]
    
#     def parse(self,response):
#         links = response.xpath("//div[@id='mian-article']/div[@class='cell medium-3 text-right']/a/@href")
#         next_page = 'https://www.nsenergybusiness.com/power/page/'+ str(dataSpider.page_number)+ '/'
   
#         for link in links:
#             yield scrapy.Request(link,self.parse_article)
                    
#     def parse_article(self, response):       
#         items = ArticleItems()
        
#         article_title = response.css('h1::text').extract()
#         article_date = response.css("#date::text").extract()
#         article_body = response.xpath("//div[@class='cell small-12 medium-12 large-10']/p/text()").extract()
#         article_body = ''.join(article_body)
#         # image_link = response.css('.tile:nth-child(3) img , .size-full , .img_caption').attr('::src').extract()

# #     # Get the list of URLs, for example:
#         items['article_title'] = article_title
#         items['article_date'] = article_date
#         items['article_body'] = article_body
#         # items['image_link'] = image_link

#         yield items

         
   