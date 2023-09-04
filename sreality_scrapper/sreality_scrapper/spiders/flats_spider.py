import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from sreality_scrapper.items import SrealityScrapperItem
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


class FlatsSpider(scrapy.Spider):
    name = 'flats'
    # start_urls = ['https://www.sreality.cz/hledani/prodej/byty?strana=3']


    def start_requests(self):
        # yield scrapy.Request(url='http://scrapy.org/', callback=self.parse)
        # settings = get_project_settings()
        # driver_path = settings['CHROME_DRIVER_PATH']

        options = webdriver.ChromeOptions()
        # options.headless = True
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")


        for number in range(1, 11):
            time.sleep(10)
            self.driver = webdriver.Chrome(options=options)
            # self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get(f"https://www.sreality.cz/hledani/prodej/byty?strana={number}")

            # with open("page_source.html", "w", encoding='utf-8') as f:
            #     f.write(driver.page_source)

            self.response = HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')

            yield scrapy.Request(url=self.driver.current_url, callback=self.parse, dont_filter=True)




    def parse(self, response):

        response = self.response
        flat_item = SrealityScrapperItem()

        for flat in response.css('div.property.ng-scope'):

            name = flat.css("a.title")
            carusel = flat.css("preact.ng-scope")

            flat_item["title"] = name.css("span.name::text").get()
            flat_item["imageurl"] = carusel.css("img::attr(src)").get()

            yield flat_item
            # # print ("title", name.css("span.name::text").get())
            # yield {"title": name.css("span.name::text").get(),
            #        "url": carusel.css("img::attr(src)").get()}

        self.driver.quit()