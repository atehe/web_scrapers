import scrapy
from itemloaders import ItemLoader
from myanimelist.items import MyanimelistItem


class AnimesSpider(scrapy.Spider):
    name = "animes"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def start_requests(self):
        for url in self.start_urls:

            yield scrapy.Request(
                url=url,
                callback=self.parse,
            )

    def parse(self, response):
        animes_url = response.xpath(
            "//h3[@class='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3']/a/@href"
        ).getall()

        for url in animes_url:
            yield response.follow(
                url=url,
                callback=self.parse_anime,
            )

        # next_page = -blue-box next"]/@href').get()
        # if next_page:
        #     yield response.follow(url=next_page, callback=self.parse)

    def parse_anime(self, response):
        loader = ItemLoader(item=MyanimelistItem(), selector=response)

        loader.add_xpath("Title", "//div[@itemprop='name']/h1/strong/text()")
        loader.add_xpath(
            "Alternative_Titles",
            "//span[@class='dark_text' and contains(text(),'Synonyms')]/parent::div/text()",
        )
        loader.add_xpath(
            "Type",
            "//span[@class='dark_text' and contains(text(),'Type')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Episodes",
            "///span[@class='dark_text' and contains(text(),'Episodes')]/parent::div/text()",
        )
        loader.add_xpath(
            "Status",
            "//span[@class='dark_text' and contains(text(),'Status')]/parent::div/text()",
        )
        loader.add_xpath(
            "Aired",
            "//span[@class='dark_text' and contains(text(),'Aired')]/parent::div/text()",
        )
        loader.add_xpath(
            "Premiered",
            "//span[@class='dark_text' and contains(text(),'Premiered')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Broadcast",
            "//span[@class='dark_text' and contains(text(),'Broadcast')]/parent::div/text()",
        )
        loader.add_xpath(
            "Producers",
            "//span[@class='dark_text' and contains(text(),'Producers')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Licensors",
            "//span[@class='dark_text' and contains(text(), 'Licensors')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Studio",
            "//span[@class='dark_text' and contains(text(), 'Studio')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Genre",
            "//span[@class='dark_text' and contains(text(), 'Genre')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Theme",
            "//span[@class='dark_text' and contains(text(), 'Theme')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Demographic",
            "//span[@class='dark_text' and contains(text(), 'Demographic')]/following-sibling::a/text()",
        )
        loader.add_xpath(
            "Duration",
            "//span[@class='dark_text' and contains(text(), 'Duration')]/parent::div/text()",
        )
        loader.add_xpath(
            "Rating",
            "//span[@class='dark_text' and contains(text(), 'Rating')]/parent::div/text()",
        )
        loader.add_xpath(
            "Source",
            "//span[@class='dark_text' and contains(text(), 'Source')]/parent::div/text()",
        )
        loader.add_xpath(
            "Score",
            "//span[@class='dark_text' and contains(text(), 'Score')]/following-sibling::span[@itemprop='ratingValue']/text()",
        )
        loader.add_xpath(
            "Score",
            "//span[@class='dark_text' and contains(text(), 'Score')]/following-sibling::span[@itemprop='ratingValue']/text()",
        )
        loader.add_xpath(
            "Scored_By",
            "//span[@class='dark_text' and contains(text(), 'Score')]/following-sibling::span[@itemprop='ratingCount']/text()",
        )
        loader.add_xpath(
            "Ranked",
            "//span[@class='dark_text' and contains(text(), 'Ranked')]/parent::div/text()",
        )
        loader.add_xpath(
            "Popularity",
            "//span[@class='dark_text' and contains(text(), 'Popularity')]/parent::div/text()",
        )
        loader.add_xpath(
            "Members",
            "//span[@class='dark_text' and contains(text(), 'Members')]/parent::div/text()",
        )
        loader.add_xpath(
            "Favorites",
            "//span[@class='dark_text' and contains(text(), 'Favorites')]/parent::div/text()",
        )
        yield loader.load_item()
