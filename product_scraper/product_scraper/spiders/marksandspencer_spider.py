import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = 'product_scraper'
    start_urls = ['https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html']

    def parse(self, response, **kwargs):
        product_data = {
            'name': response.css('h1.product-name::text').get(),
            'price': float(response.css('span.value::attr(content)').get()),
            'color': response.css('div.colour-picker::attr(data-colorname)').get(),
            'size': response.css('select.select-size option::text').getall(),
            'reviews_count': response.css('span.review-summary-count::text').get(),
            'reviews_score': response.css('span.review-summary__rating::text').get(),
        }

        output_filename = 'product_data.json'
        with open(output_filename, 'w') as f:
            json.dump(product_data, f, indent=4)

        self.log(f'Saved data to {output_filename}')
