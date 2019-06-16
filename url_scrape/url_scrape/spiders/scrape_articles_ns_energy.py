import scrapy
import csv
from ..items import ArticleItems
import spacy

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
        nlp = spacy.load("en_core_web_sm")   
        items = ArticleItems()
        # scraping article title, date, body , image url and tags for the articles
        article_title = response.css('h1::text').extract()
        article_date = response.css("#date::text").extract()
        article_content = response.xpath("//div[@class='cell small-12 medium-12 large-10']/p/text()").extract()
        article_content = ''.join(article_content) 
        
        entity = nlp(article_content)
        #scraping the countries and companies using spacy library
        for ent in entity.ents:
            if ent.label_ == 'ORG':
                organisation = ent.text
            if ent.label_ == 'GPE':
                country = ent.text
        image_link = response.xpath("//div[@class='cell small-12 medium-12 large-10']/img/@src").extract()
        category_1 = response.xpath("//p[@class='tags']/span[1]/a/text()").extract_first()
        category_2 = response.xpath("//p[@class='tags']/span[2]/a/text()").extract_first()
        category_3 = response.xpath("//p[@class='tags']/span[3]/a/text()").extract_first()
    
        items['image_link'] = image_link
        items['category_1'] = category_1
        items['category_2'] = category_2
        items['category_3'] = category_3
        items['Country']   = country
        items['Company'] = organisation
        items['article_content'] = article_content
        items['article_date'] = article_date
        items['article_title'] = article_title
        yield items
        
   