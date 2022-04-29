import scrapy
from urllib.parse import quote
from scrapy.utils.response import open_in_browser

categories = {
    "Cabinet d'études",
    "Grande distribution",
    "Assurances",
    "Banque",
    "BTP",
    "Coffrets cadeaux",
    "Assurance",
    "Energie",
    "Informatique",
    "Crédit",
    "Jeux",
    "Matériel Télécommunication",
    "Meubles",
    "Prêt à porter",
    "Telecom",
    "Télévision",
    "Tourisme",
    "Vente en ligne",
    "Electroménager",
    "Location de voiture",
    "Papeterie",
}
# "Fournitures de bureau",
# "Matériel de bureau",
# "parfums",
# "maquillage",
# "soins",
# "Associations",
# "Plateforme de mise en relation",
# "Nouvelles technologies d'informations",
# "Automobiles",
# "Gestion de l'informations",
# "Sondage",
# "agence de voyage",
# "hôtel",
# "Vente en ligne",
# "e-commerce",
# "Location de voiture",
# "Papeterie, fournitures et matériel de bureau",
# "parfum",
# "Automobiles",
# }
location = "Paris ON"


class CategoriesSpider(scrapy.Spider):
    name = "categories"
    allowed_domains = ["yellowpages.ca"]

    def start_requests(self):
        for category in categories:
            url = f"https://www.yellowpages.ca/search/si/1/{quote(category).strip()}/{quote(location).strip()}"
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"category": category, "location": location},
            )

    def parse(self, response):
        companies = response.xpath("//div[@class='listing_right_section']")

        for company in companies:
            yield {
                "Name": company.xpath(".//h3/a/text()").get(),
                "Address": ",".join(
                    company.xpath(
                        ".//span[contains(@itemprop, 'address')]/span/text()"
                    ).getall()
                ),
                "business": ",".join(
                    company.xpath(
                        ".//div[@class='listing__headings']/a/text()"
                    ).getall()
                ),
                "phone number": company.xpath(
                    ".//li[contains(@class, 'mlr__item--phone')]//h4/text()"
                ).getall(),
                "website redirect url": company.xpath(
                    ".//li[contains(@class, 'mlr__item--website')]/a/@href"
                ).get(),
                "category": response.meta.get("category"),
                "location": response.meta.get("location"),
            }
