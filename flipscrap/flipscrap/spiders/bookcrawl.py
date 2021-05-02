import scrapy
from ..items import FlipscrapItem
from scrapy.loader import ItemLoader


class EcomdetailsSpider(scrapy.Spider):
    name = 'bookscrap'
    page_number = 2
    start_urls = [
        "https://www.flipkart.com/search?q=books"
        ]

    def parse(self, response):
        products = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_4ddWXP", " " ))]')
        for product in products:
            l = ItemLoader(item=FlipscrapItem(), selector=product)
            l.add_css('name', '.s1Q9rs::text')
            l.add_css('author_format', '._3Djpdu::text')
            l.add_css('rating', '._1lRcqv ._3LWZlK::text')
            l.add_css('price', '._8VNy32 ._30jeq3::text')
            l.add_css('image','._3exPp9::attr(src)')

            yield l.load_item()


        next_page =  "https://www.flipkart.com/search?q=books&page=" + str(EcomdetailsSpider.page_number) 
        if EcomdetailsSpider.page_number <= 4:
            EcomdetailsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
