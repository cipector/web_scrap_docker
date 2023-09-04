from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sreality_scrapper.spiders.flats_spider import FlatsSpider

process = CrawlerProcess(get_project_settings())
process.crawl(FlatsSpider)
process.start()