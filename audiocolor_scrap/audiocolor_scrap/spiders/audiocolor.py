import scrapy

class ProductsAudiocolor(scrapy.Spider):
    name = "audiocolor"
    start_urls = [
        "https://www.audiocolor.co/categoria/gamer/"
        
    ]

    custom_settings = {
        'FEEDS': {
            'audiocolor_gamer.json': {
                'format': 'json',
                'encoding': 'utf8'
            },
        },
        # 'CONCURRENT_REQUEST': 24, 
        # 'MEMUSAGE_LIMIT_MB': 2048,
        'USER_AGENT': 'Copi',
        'ROBOTSTXT_OBE': True  
    }
    
    title_article_link = '//h3[@class="jet-woo-builder-archive-product-title"]/a/@href'
    cargar_mas_button = '//div[@class="elementor-button-wrapper"]/a/@href'

    def parse(self, response):
        title_article_link = response.xpath(self.title_article_link).extract()
        cargar_mas_button_link = response.xpath(self.cargar_mas_button).extract_first()

        yield {
            'title_article_link': title_article_link
            }

        if cargar_mas_button_link:
            yield response.follow(cargar_mas_button_link, callback=self.parse_articles, cb_kwargs={'title_article_link': title_article_link})

    def parse_articles(self, response, **kwargs):
        if kwargs:
            title_article_link = kwargs['title_article_link']
        
        title_article_link.extend(response.xpath(self.title_article_link).extract())

        cargar_mas_button_link = response.xpath(self.cargar_mas_button).extract_first()

        if cargar_mas_button_link:
            yield response.follow(cargar_mas_button_link, callback=self.parse_articles, cb_kwargs={'title_article_link': title_article_link})
        else:
            yield {
                'title_article_link': title_article_link
            }

