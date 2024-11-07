import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["krasnoyarsk.lemanapro.ru"]
    start_urls = ["https://krasnoyarsk.lemanapro.ru/catalogue/lyustry/"]

    def parse(self, response):
        pass
