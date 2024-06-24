import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
import json


class ProductSpider(scrapy.Spider):
    name = 'product_scraper'
    start_urls = ['https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html']

    def __init__(self, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, response, **kwargs):
        self.driver.get(response.url)
        self.driver.implicitly_wait(10)

        response = HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')

        product_data = {
            'name': response.css('h1.product-name::text').get(),
            'price': float(response.css('span.value::attr(content)').get()),
            'color': response.css('div.colour-picker::attr(data-colorname)').get(),
            'size': response.css('select.select-size option::text').getall(),
            'reviews_count': int(response.css('span.review-summary-count::attr(data-value)').get()),
            'reviews_score': float(response.css('span.review-summary__rating::attr(data-value)').get()),
        }

        output_filename = 'product_data.json'
        with open(output_filename, 'w') as f:
            json.dump(product_data, f, indent=4)

        self.log(f'Saved data to {output_filename}')
        self.driver.quit()

    def closed(self, reason):
        self.driver.quit()
