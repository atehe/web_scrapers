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
                url=url,
                callback=self.parse_anime,
                meta={"name": name},
                headers={"User-Agent": self.user_agent},
            )

    def parse_anime(self, response):

        name = response.request.meta["name"]

        yield {
            "Name": name,
            "Type": response.xpath(
                "//h2[text()='Information']/following-sibling::div[1]/a/text()"
            ).get(),
            "Episodes": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[2]/text()"
                ).getall()
            ).strip("\n "),
            "Status": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[3]/text()"
                ).getall()
            ).strip("\n "),
            "Aired": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[4]/text()"
                ).getall()
            ).strip("\n "),
            "Premiered": response.xpath(
                "//h2[text()='Information']/following-sibling::div[5]/a/text()"
            ).get(),
            "Broadcast": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[6]/text()"
                ).getall()
            ).strip("\n "),
            "Producers": response.xpath(
                "//h2[text()='Information']/following-sibling::div[7]/a/text()"
            ).getall(),
            "Licensors": response.xpath(
                "//h2[text()='Information']/following-sibling::div[8]/a/text()"
            ).get(),
            "Studios": response.xpath(
                "//h2[text()='Information']/following-sibling::div[9]/a/text()"
            ).get(),
            "Source": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[10]/text()"
                ).getall()
            ).strip("\n "),
            "Genres": response.xpath(
                "//h2[text()='Information']/following-sibling::div[11]/a/text()"
            ).getall(),
            "Themes": response.xpath(
                "//h2[text()='Information']/following-sibling::div[12]/a/text()"
            ).getall(),
            "Demographic": response.xpath(
                "//h2[text()='Information']/following-sibling::div[13]/a/text()"
            ).get(),
            "Duration": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[14]/text()"
                ).getall()
            ).strip("\n "),
            "Rating": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[15]/text()"
                ).getall()
            ).strip("\n "),
            "Score": response.xpath(
                "//h2[text()='Information']/following-sibling::div[16]/span[2]/text()"
            ).get(),
            "Scored By": response.xpath(
                "//h2[text()='Information']/following-sibling::div[16]/span[3]/text()"
            ).get(),
            "Ranked": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[17]/text()"
                ).getall()
            ).strip("\n "),
            "Popularity": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[18]/text()"
                ).getall()
            ).strip("\n "),
            "Members": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[19]/text()"
                ).getall()
            ).strip("\n "),
            "Favorites": "".join(
                response.xpath(
                    "//h2[text()='Information']/following-sibling::div[20]/text()"
                ).getall()
            ).strip("\n "),
        }
