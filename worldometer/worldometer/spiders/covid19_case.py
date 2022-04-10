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
        print(response.body)


# script = """
#     function main(splash, args)
#         assert(splash:go(args.url))
#         assert(splash:wait(10))
#         splash:set_viewport_full()
#         return {
#             html = splash:html()
#         }
#     end
#     """
# print(
#     SplashRequest(
#         url="https://www.worldometers.info/coronavirus",
#         endpoint="execute",
#         args={"lua_source": script},
#     )
# )
