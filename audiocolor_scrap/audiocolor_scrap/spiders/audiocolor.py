import scrapy

class ProductsAudiocolor(scrapy.Spider):
    name = "products"
    start_urls = [
        "https://www.audiocolor.co/categoria/gamer"
    ]

    custom_settings = {
        'FEEDS': {
            'gamer.json': {
                'format': 'json',
                'encoding': 'utf8'
            },
        },
        'CONCURRENT_REQUEST': 24, 
        'MEMUSAGE_LIMIT_MB': 2048,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'ROBOTSTXT_OBE': True  
    }
    
    title = '//div[@class="product-description"]/h3/a/text()'

    def parse(self, response):
        title = response.xpath(self.title).extract()

        print('*' * 100)
        self.logger.info('Response status: %s' % response.status)
        print('*' * 100)

        # self.logger.info('Response content: %s' % response.body)

        yield {
            'title': title
        }
    