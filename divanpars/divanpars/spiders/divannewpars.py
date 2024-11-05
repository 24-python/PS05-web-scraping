import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["hhttps://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        pass
