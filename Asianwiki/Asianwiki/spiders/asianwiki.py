import scrapy, bs4, requests, time
from requests_html import HTMLSession

url = "https://www.sabishare.com/file/sFuWPdYNi64-the-last-kingdom-s03e01-netnaija-com-mp4"

try:
    session = HTMLSession()
    response = session.get(url)
except requests.exceptions.RequestException as error:
    print(error)

response.html.render(timeout=100)


print(response.html.find("a", {"class": "download-url"}))
