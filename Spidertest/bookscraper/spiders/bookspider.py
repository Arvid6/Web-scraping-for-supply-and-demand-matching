import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"] #gör så vi endast scrapar den websidan vi vill går inte iväg till andra länkar
    start_urls = ["https://books.toscrape.com"] #start URL (kan ha flera)

    def parse(self, response): # kallas på när svar kommer tbx
        books = response.css('article.product_pod')
        for book in books:
            yield{
                'name' : book.css('h3 a::text').get(),
                'price' : book.css('.product_price .price_color::text').get(),
                'url' : book.css('h3 a').attrib['href'],
            }
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)