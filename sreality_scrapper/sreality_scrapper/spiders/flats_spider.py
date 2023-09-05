import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from sreality_scrapper.items import SrealityScrapperItem
from selenium.webdriver.chrome.service import Service


class FlatsSpider(scrapy.Spider):
    name = 'flats'

    def start_requests(self):

        options = webdriver.ChromeOptions()
        # options.headless = True
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        service = Service()

        for number in range(1, 41):
            time.sleep(20)
            self.driver = webdriver.Chrome(service=service, options=options)
            # self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get(f"https://www.sreality.cz/hledani/prodej/byty?strana={number}")

            # with open("page_source.html", "w", encoding='utf-8') as f:
            #     f.write(driver.page_source)

            self.response = HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')

            yield scrapy.Request(url="https://quotes.toscrape.com/", callback=self.parse, dont_filter=True)




    def parse(self, response):

        response = self.response
        flat_item = SrealityScrapperItem()

        for flat in response.css('div.property.ng-scope'):

            name = flat.css("a.title")
            carusel = flat.css("preact.ng-isolate-scope")

            flat_item["title"] = name.css("span.name::text").get()
            flat_item["imageurl"] = carusel.css("img::attr(src)").extract()[3]

            yield flat_item

        self.driver.quit()