from scrapy import cmdline


def crawl():
    cmdline.execute("scrapy crawl vacancies -O jobs.csv".split())


if __name__ == "__main__":
    crawl()
