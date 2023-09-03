import scrapy
from selenium import webdriver




class FlatsSpider(scrapy.Spider):
    name = 'flats'

    def start_requests(self):
        # settings = get_project_settings()
        # driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = False
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.sreality.cz/hledani/prodej/byty?strana=3')
        body_html = driver.execute_script("return document.body.innerHTML")

        driver.quit()
        # print(body_html)
        # with open('page_content.html', 'w') as f:
        #     f.write(body_html)

        # response = scrapy.http.HtmlResponse(url="my HTML string", body=body_html, encoding='utf-8')
        # # self.pokus(body_html)
        # for flat in response.css('div.property ng-scope'):
        #     yield {"name": flat.css("a.title::text").get()}

        flats = scrapy.Selector(text=body_html)
        flats.xpath('//div//property ng-scope').extract()

        for flat in flats:
            print({flat.scrapy.css("a.title::text").get()})

    # def parse(self, response):

            # l = ItemLoader(item = WhiskyscraperItem(), selector=products)
            #
            # l.add_css('name', 'a.product-item-link')
            # l.add_css('price', 'span.price')
            # l.add_css('link', 'a.product-item-link::attr(href)')
            #
            # yield l.load_item()


        # next_page = response.css('a.action.next').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)



# import scrapy
# from whiskyscraper.items import WhiskyscraperItem
# from scrapy.loader import ItemLoader
#
#
# class WhiskeySpider(scrapy.Spider):
#     name = 'whisky'
#     start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']
#
#     def parse(self, response):
#         for products in response.css('div.product-item-info'):
#             l = ItemLoader(item = WhiskyscraperItem(), selector=products)
#
#             l.add_css('name', 'a.product-item-link')
#             l.add_css('price', 'span.price')
#             l.add_css('link', 'a.product-item-link::attr(href)')
#
#             yield l.load_item()
#
#
#         next_page = response.css('a.action.next').attrib['href']
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)%