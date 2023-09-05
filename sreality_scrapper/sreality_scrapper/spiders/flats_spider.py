import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from sreality_scrapper.items import SrealityScrapperItem
from selenium.webdriver.chrome.service import Service
import random


class FlatsSpider(scrapy.Spider):
    name = 'flats'
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': 550,
    }

    def start_requests(self):

        options = webdriver.ChromeOptions()
        # options.headless = True
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        service = Service()

        for number in range(1, 101):
            time.sleep(20+random.randint(0,15))
            self.driver = webdriver.Chrome(service=service, options=options)
            # self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get(f"https://www.sreality.cz/hledani/prodej/byty?strana={number}")

            # with open("page_source.html", "w", encoding='utf-8') as f:
            #     f.write(driver.page_source)

            self.response = HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')

            yield scrapy.Request(url=self.driver.current_url, callback=self.parse, dont_filter=False)




    def parse(self, response):

        try:
            response = self.response
            flat_item = SrealityScrapperItem()

            for flat in response.css('div.property.ng-scope'):

                name = flat.css("a.title")
                carusel = flat.css("preact.ng-isolate-scope")

                flat_item["title"] = name.css("span.name::text").get()
                flat_item["imageurl"] = carusel.css("img::attr(src)").extract()[3]

                yield flat_item

        except Exception as error:
            self.logger.error(str(error))

        self.driver.quit()