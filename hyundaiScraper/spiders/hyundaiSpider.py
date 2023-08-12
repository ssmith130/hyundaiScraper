import scrapy


class HyundaispiderSpider(scrapy.Spider):
    name = "hyundaiSpider"
    allowed_domains = ["www.hyundaiusa.com"]
    start_urls = ["https://www.hyundaiusa.com/us/en"]

    def parse(self, response):
        pass
