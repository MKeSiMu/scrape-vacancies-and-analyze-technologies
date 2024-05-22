import scrapy


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["www.work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/?page=1"]

    def parse(self, response):
        pass
