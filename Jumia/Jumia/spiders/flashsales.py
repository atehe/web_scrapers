import scrapy
import logging

class FlashsalesSpider(scrapy.Spider):
    name = "flashsales"
    allowed_domains = ["www.jumia.com.ng"]
    start_urls = ["http://www.jumia.com.ng/flash-sales/"]
    page_num = 1

    def parse(self, response):
        logging.info(f'\nSCRAPING PAGE {self.page_num}\n')
        self.page_num += 1
        
        products = response.xpath("//section/div/article")

        for product in products:
            product_url = product.xpath(".//a/@href").get()
            product_name = product.xpath(".//a/@data-name").get()
            
            if product_url == None:
                continue

            yield response.follow(
                url=product_url,
                callback=self.parse_product,
                meta={"product_name": product_name},
            )
        
        next_page = response.xpath("//a[@aria-label='Next Page']/@href").get()
        if next_page:
            yield response.follow(
                url=next_page,
                callback=self.parse
            )

    def parse_product(self, response):
        yield {
            'product_name': response.request.meta["product_name"],
            'product_brand': response.xpath("//div[@class='-pvxs']/a[1]/text()").get(),
            'product_rating': response.xpath("//div[@class='stars _s _al']/text()").get(),
            'verified_ratings': response.xpath("//a[@class='-plxs _more']/text()").get(),
            'items_left': response.xpath(
                '//div[@class="-pas -brbl-rd6 -rad4-bot"]/div[2]/span/text()'
            ).get(),
            'current_price': response.xpath(
                "//div[@class='-pas -brbl-rd6 -rad4-bot']/span/text()"
            ).get(),
            'previous_price': response.xpath(
                '//div[@class="-pas -brbl-rd6 -rad4-bot"]/div[1]/span[1]/text()'
            ).get(),
            'discount': response.xpath(
                '//div[@class="-pas -brbl-rd6 -rad4-bot"]/div[1]/span[2]/text()'
            ).get(),    
        }
       