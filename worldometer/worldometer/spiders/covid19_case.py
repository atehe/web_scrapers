import scrapy
from scrapy_splash import SplashRequest
from scrapy.utils.response import open_in_browser


class Covid19CaseSpider(scrapy.Spider):
    name = "covid19_case"
    allowed_domains = ["www.worldometers.info"]

    script = """
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(10))
        splash:set_viewport_full()
        return {
            html = splash:html()
        }
    end 
    """

    def start_requests(self):
        yield SplashRequest(
            url="https://www.worldometers.info/coronavirus",
            callback=self.parse,
            endpoint="execute",
            args={"lua_source": self.script},
        )

    def parse(self, response):
        table_rows = response.xpath(
            '//*[@id="main_table_countries_today"]/tbody[1]/tr[@style!="display: none"]'
        )
        # print(table_rows)
        for row in table_rows:
            yield {
                "Country": row.xpath("./td[2]/a/text()").get()
                or row.xpath("./td[2]/span/text()").get(),
                "Total Cases": row.xpath("./td[3]/text()").get(),
                "New Cases": row.xpath("./td[4]/text()").get(),
                "Total Deaths": row.xpath("./td[5]/text()").get(),
                "New Deaths": row.xpath("./td[6]/text()").get(),
                "Total Recovered": row.xpath("./td[7]/text()").get(),
                "New Recovered": row.xpath("./td[8]/text()").get(),
                "Active Cases": row.xpath("./td[9]/text()").get(),
                "Serious, Critical": row.xpath("./td[10]/text()").get(),
                "Total Test": row.xpath("./td[13]/text()").get(),
                "Population": row.xpath("./td[15]/a/text()").get()
                or row.xpath("./td[15]/text()").get(),
                "Continent": row.xpath("./td[16]/text()").get(),
            }
