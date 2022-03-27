import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import SitemapSpider, Rule

from movie_scraper.items import Celebrity


class RottenTomatoSpider(SitemapSpider):
    name = 'rotten_tomato'
    sitemap_urls = ['https://www.rottentomatoes.com/sitemaps/sitemap.xml']
    sitemap_rules = [
        ('/celebrity/', 'parse_celebrity')
    ]

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
    
    def parse_celebrity(self, response):
        item = Celebrity()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        item['name'] = response.xpath('//h1[@data-qa="celebrity-bio-header"]/text()').get(0)
        item['highest_rated'] = response.xpath('//p[@data-qa="celebrity-bio-highest_rated"]/span/a/text()').get(0)
        item['lowest_rated'] = response.xpath('//p[@data-qa="celebrity-bio-lowest_rated"]/span/a/text()').get(0)
        item['birthday'] = response.xpath('normalize-space(//p[@data-qa="celebrity-bio-bday"]/text())').get(0).strip()
        item['birthplace'] = response.xpath('normalize-space(//p[@data-qa="celebrity-bio-birthplace"]/text())').get(0).strip()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
