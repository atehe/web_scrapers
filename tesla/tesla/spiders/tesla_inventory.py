import scrapy
import json


class TeslaInventorySpider(scrapy.Spider):
    name = "tesla_inventory"
    allowed_domains = ["www.tesla.com/inventory"]
    start_urls = [
        'https://www.tesla.com/inventory/api/v1/inventory-results?query={"query":{"model":"ms","condition":"used","options":{},"arrangeby":"Price","order":"asc","market":"US","language":"en","super_region":"north america","lng":-121.8918364,"lat":37.3326639,"zip":"95113","range":0,"region":"CA"},"offset":0,"count":50,"outsideOffset":0,"outsideSearch":false}'
    ]

    def parse(self, response):
        inventory_items = json.loads(response.body)
        print(len(inventory_items))
