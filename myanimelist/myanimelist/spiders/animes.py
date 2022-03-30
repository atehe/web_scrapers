import scrapy
import cfscrape
from scrapy.utils.response import open_in_browser
import re


def clean_score_data(score_data):
    score_pattern = r"\d\.\d\d"
    score_match = re.search(score_pattern, score_data)

    if score_match:
        score = score_match.group()
        scored_by_pattern = r"\d{0,3},{0,1}\d{0,3},\d{3}"
        scored_by_match = re.search(scored_by_pattern, score_data)
        scored_by = scored_by_match.group()

        return f"{score} scored by {scored_by} users"


def clean_xpath_data(data):
    invalid_data = [",", "\n", ""]
    data = [elem.strip().strip("\n").strip(",") for elem in data]
    valid_data = [elem for elem in data if elem not in invalid_data]
    info_header = [elem[:-1] for elem in valid_data if elem[-1] == ":"]
    if len(info_header) == 1:
        info_name = info_header[0]
        info_data_list = set(valid_data[1:])
        info_data = ", ".join(info_data_list)

        if info_name == "Theme":
            info_name = "Themes"
        elif info_name == "Score":
            info_data = clean_score_data(info_data)
        return info_name, info_data


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
        next_page = response.xpath('//a[@class="link-blue-box next"]/@href').get()
        # if next_page:
        #     response.follow(
        #         url=next_page,
        #         callback=self.parse,
        #         headers={"User-Agent": self.user_agent},
        #     )

    def parse_anime(self, response):
        name = response.request.meta["name"]
        info_dict = {"Name": name}

        info_xpaths = response.xpath(
            "//h2[text()='Information']/following-sibling::div"
        )

        for info in info_xpaths:
            data = info.xpath(".//text()").getall()
            info_data = clean_xpath_data(data)
            if not info_data:
                continue
            info_dict[info_data[0]] = info_data[1]

        yield info_dict
