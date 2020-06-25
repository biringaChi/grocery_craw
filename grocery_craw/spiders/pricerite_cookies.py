import scrapy


class PriceriteCookiesSpider(scrapy.Spider):
    name = 'pricerite_cookies'
    allowed_domains = ['https://www.instacart.com/store/pricerite/departments/3884/aisles/29703']
    start_urls = ['http://https://www.instacart.com/store/pricerite/departments/3884/aisles/29703/']

    def parse(self, response):
        pass
