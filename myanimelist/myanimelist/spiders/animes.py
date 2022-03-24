import scrapy
import cfscrape
from scrapy.utils.response import open_in_browser


class AnimesSpider(scrapy.Spider):
    name = "animes"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"

    def start_requests(self):
        for url in self.start_urls:

            yield scrapy.Request(
                url=url,
                headers={"User-Agent": self.user_agent},
                callback=self.parse,
            )

    def parse(self, response):
        animes = response.xpath("//tr[@class='ranking-list']/td[2]/div/div[2]/h3")

        for anime in animes:
            name = anime.xpath("./a/text()").get()
            url = anime.xpath("./a/@href").get()

            yield response.follow(
                url=url, callback=self.parse_anime, meta={"name": name}
            )

    def parse_anime(self, response):

        name = response.request.meta["name"]
        print(name)
