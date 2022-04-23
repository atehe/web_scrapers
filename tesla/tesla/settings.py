# Scrapy settings for tesla project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "tesla"

SPIDER_MODULES = ["tesla.spiders"]
NEWSPIDER_MODULE = "tesla.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tesla (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookies": 'ak_bmsc=172915B990D86F9A24008CCA35FE9266~000000000000000000000000000000~YAAQVUwQAv3iTz+AAQAApjiQSw/eC2T3gtTsdsA+//K4HW3g4VqiMzhHl7je1hKmwWFiifEkoCYB4SRiAohYxTHMLqAkaQb+j+tQNpjqr/SrRJBrC3kUdun7iGHz7HWtuUBuSe1PyvYbinc+HFS2p1q9Yg41nxwFwgTqAv0a7xPTMaK87QRjzVq1NlcG+jq/p9FyOboZnlpMAVMAPALZiGvtlcY+gGsa+0gJwq0bmON5U+HhI70nu5sila9fkQSneb3BVDine5P1EwGA+eQ7OnOYwWLtUvl5FNGW+zgKP0u5knSeqPIpujNS7SKyzMoQF1xOiBUSnTzfiGZ5A9WeHKMf4RERJI7bQZ3jQ1eHi9OctckMSus1jNT86tvc1pvDHdG7bsCl4obN; _gid=GA1.2.1753173834.1650535187; coin_auth=b85ca1b5e66a82b9c40fcb144ffa26bb; ip_info={"ip":"102.89.32.62","location":{"latitude":10,"longitude":8},"region":null,"city":"","country":"Nigeria","countryCode":"NG","postalCode":""}; _ga_KFP8T9JWYJ=GS1.1.1650535186.1.1.1650539386.0; bm_sv=A900AFEEC7551EFE21127274347C6A27~umfPIIFYNbCabnXeMy0E1Y9eWc2Ph6scED0iOd59a2U0ClDhkY0SNfBhh1BUDXk9j+b1As0nmTB9Kq68hh31+qQGKfoDtpjX2DYytAsSy48/EomMstz/I1pnxgdrvJU/wwpQ44yQvH9eBzUFXMC8MRf2TJ+H3K9PjO9g6UvmlIw=; _ga=GA1.2.1853355029.1650535187',
    "if-none-match": 'W/""1649812546-430709244""',
    "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tesla.middlewares.TeslaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'tesla.middlewares.TeslaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'tesla.pipelines.TeslaPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
