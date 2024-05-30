import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    print("scraping starts")
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        # Extract movie details
        for movie in response.css('td.titleColumn')[:50]:  # Limiting to top 50 movies
            title = movie.css('a::text').get()
            year = movie.css('span.secondaryInfo::text').get().strip('()')
            rating = movie.xpath('following-sibling::td[contains(@class, "ratingColumn")]/strong/text()').get()
            star_cast = movie.css('a::attr(title)').get()
            yield {
                'title': title,
                'year': year,
                'rating': rating,
                'star_cast': star_cast,
            }

        # Handle pagination if needed (not required for top 50 as it's on a single page)