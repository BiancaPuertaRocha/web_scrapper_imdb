import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        # name_year = response.css('.titleColumn')
        # names = response.css('.titleColumn a ::text').getall()
        # years = response.css('.secondaryInfo ::text').getall()
        # rating = response.css('strong ::text').getall()
        for filme in response.css('.lister-list tr'):
            yield { 
                'name': filme.css('.titleColumn a ::text').get(),
                'year': filme.css('.secondaryInfo ::text').get()[1:-1],
                'rating': filme.css('strong ::text').get()
            }

        
