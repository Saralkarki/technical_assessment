import scrapy
import csv
from ..items import ArticleItems
import spacy

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
        nlp = spacy.load("en_core_web_sm")         
        items = ArticleItems()
        # scraping article title, date, body , image url and tags for the articles
        
        article_title = response.css('.entry-title::text').extract()
        article_date = response.css(".td-post-title .td-module-date::text").extract()
        article_content = response.css("p,strong").css('::text').extract()
        article_content = ''.join(article_content)       
        image_link = response.xpath("//div[@class='td-post-featured-image']/figure/a/@href").extract()
        category_1 = response.xpath("//li[1][@class='entry-category']/a/text()").extract()   
        category_2 = response.xpath("//li[2][@class='entry-category']/a/text()").extract()
        category_3 = response.xpath("//li[3][@class='entry-category']/a/text()").extract()
        #scraping the countries and companies using spacy library
        entity = nlp(article_content)
        for ent in entity.ents:
            if ent.label_ == 'ORG':
                organisation = ent.text
            if ent.label_ == 'GPE':
                country = ent.text

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
        
   