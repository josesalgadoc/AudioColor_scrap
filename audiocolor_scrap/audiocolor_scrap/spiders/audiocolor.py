import scrapy

class ProductsAudiocolor(scrapy.Spider):
    name = "products"
    start_urls = [
        "https://www.falabella.com.co/falabella-co/category/cat3050947/SmartWatch"
        # "https://www.audiocolor.co/categoria/gamer"
        
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
        'USER_AGENT': 'Copi',
        'ROBOTSTXT_OBE': True  
    }
    
    # title = '//div[@class="product-description"]/h3/a/text()'
    
    # test = response.xpath('//div[@class="elementor-inner"]//div[@class="elementor-widget-wrap"]//div[@class="elementor-widget-cotainer"]/h3[@class="jet-woo-builder-archive-product-title"]/a/@href').extract()
    
    # accesories = response.xpath('//div[@class="elementor-inner"]//div[@class="elementor-container elementor-column-gap-default"]//div[@class="jet-listing-grid jet-listing"]//div[@class="slick-list draggable"]//div[@class="elementor-widget-container"]/h2/text()').extract()
    
    # ktronix = response.xpath('//div[@cclass="plp__result-slot plp__result-slot--list"]//div[@class="ais-InfiniteHits product__listing"]//li[@class="ais-InfiniteHits-item product__item js-product-item js-algolia-product-click"]/h3[@class="product__item__top__title"]/a/text()').extract()
    
    # ktronix = response.xpath('//div[@class="plp__result-slot plp__result-slot--list"]//div[@class="ais-InfiniteHits product__listing"]//li[@class="ais-InfiniteHits-item product__item js-product-item js-algolia-product-click"]/h3/a/text()').extract()

    # falabella_smartwatch = '//div[@class="jsx-1250940326 pod-group--container container"]//div[@id="testId-searchResults-products" and @class="jsx-4099777552 search-results--products"]//div[@pod-layout="4_GRID" and @class="jsx-4001457643 search-results-4-grid grid-pod"]//a/@href'

    falabella_title = '//div[@class="Header-module_header-util-bar__1Qt0E"]//div[@class="MediaComponent-module_tablet-desktop__3xCIl"]//span[@class="HamburgerBtn-module_title__26h1r"]/text()'

    def parse(self, response):
        falabella = response.xpath(self.falabella_title).extract()

        # print('*' * 100)
        # self.logger.info('Response status: %s' % response.status)
        # print('*' * 100)

        print('*' * 100)
        self.logger.info('Response content: %s' % response.body)
        print('*' * 100)

        yield {
            'title': falabella
        }
    