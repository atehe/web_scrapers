from curses.ascii import HT
import scrapy, bs4, requests, time
from requests_html import HTMLSession

url = "https://asianwiki.com/Category:SBS_Drama_Series"

try:
    session = HTMLSession()
    response = session.get(url)
except requests.exceptions.RequestException as error:
    print(error)

response.html.render()

time.sleep(10)
soup = bs4.BeautifulSoup(response.text, "html.parser")
print(soup)
