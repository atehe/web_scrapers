import scrapy


class PopulationSpider(scrapy.Spider):
    name = "population"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country/"
    ]

    def parse(self, response):
        countries_elem = response.xpath("//td/a")

        for country_elem in countries_elem:
            country_name = country_elem.xpath("./text()").get()
            country_link = country_elem.xpath("./@href").get()

            yield response.follow(
                url=country_link,
                callback=self.parse_country,
                meta={"country": country_name},
            )

    def parse_country(self, response):
        country = response.request.meta["country"]
        rows = response.xpath(
            "(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr"
        )

        for row in rows:
            year = row.xpath("(./td)[1]/text()").get()
            population = row.xpath("(./td)[2]/strong/text()").get()

            yield {"country": country, "year": year, "population": population}
