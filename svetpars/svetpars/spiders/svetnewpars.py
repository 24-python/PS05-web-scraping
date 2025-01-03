import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://www.divan.ru/krasnoyarsk"]
    start_urls = ["https://www.divan.ru/krasnoyarsk/category/svet"]

    def parse(self, response):
        svets = response.css('div.WdR1o')

        for svet in svets:
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'url': svet.css('a::attr(href)').get()
            }