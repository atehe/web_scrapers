import scrapy


class UkHotelsSpider(scrapy.Spider):
    name = "uk_hotels"
    allowed_domains = ["www.booking.com"]
    start_urls = [
        "https://www.booking.com/searchresults.html?aid=304142&label=gen173rf-1FCAEoggI46AdIM1gDaKcBiAEBmAExuAEZyAEM2AEB6AEB-AECiAIBogIKdXB3b3JrLmNvbagCA7gCj_H0kgbAAgHSAiQ0Nzc2OGFjNy1hZDU1LTQ4Y2MtODk4MS0xZDZkYTcxNWVlMDHYAgXgAgE&sid=7cc1c3af8fec962eea2ba75b24a6c95c&sb=1&sb_lp=1&src=theme_landing_index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fhotel%2Findex.html%3Faid%3D304142%3Blabel%3Dgen173rf-1FCAEoggI46AdIM1gDaKcBiAEBmAExuAEZyAEM2AEB6AEB-AECiAIBogIKdXB3b3JrLmNvbagCA7gCj_H0kgbAAgHSAiQ0Nzc2OGFjNy1hZDU1LTQ4Y2MtODk4MS0xZDZkYTcxNWVlMDHYAgXgAgE%3Bsid%3D7cc1c3af8fec962eea2ba75b24a6c95c%3Bsrpvid%3D27694e00d88b0079%26%3B&ss=United+Kingdom&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=un&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=222&dest_type=country&place_id_lat=54.4983&place_id_lon=-3.07394&search_pageview_id=f3844e06aad30343&search_selected=true&search_pageview_id=f3844e06aad30343&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
    ]

    def parse(self, response):
        pass
