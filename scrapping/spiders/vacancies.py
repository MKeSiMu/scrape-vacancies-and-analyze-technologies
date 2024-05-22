import scrapy
from scrapy.http import Response


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    custom_settings = {
        "USER_AGENT": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
        ),
        "DOWNLOAD_DELAY": 2,
    }
    allowed_domains = ["www.work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/?page=1"]
    page_number = 2

    def parse(self, response: Response, **kwargs) -> dict:
        job_page_links = response.css("h2 > a::attr(href)")
        yield from response.follow_all(job_page_links, self.parse_work_ua)

        # go to next page
        if job_page_links:
            next_page = f"https://www.work.ua/jobs-python/?page={self.page_number}"
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
            self.page_number += 1

    @staticmethod
    def parse_work_ua(response: Response) -> dict:
        yield {
            "title": (
                "".join(
                    response.css(
                        "h1#h1-name::text, h1#h1-name span.highlight-result::text"
                    ).getall()
                )
            ),
            "description": response.css("ul.js-toggle-block li span::text").getall()
        }
