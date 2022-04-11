## Scraper for Worldometer
[Worldometer](https://www.worldometers.info/about/) is a website run with the goal of making world statistics available in time relevant format. 
This project contains two spiders, one  to scrape the content of the historic population statistics of countries and another to scrape the real time covid 19 data of countries.

## Requirements
The covid 19 data is rendered using javascript and thus requires scrapy-splash to scrape its content. On the other hand scrapy-splash uses splash HTTP API so it needs docker installed on host system to run.
See the scrapy-splash documentation [here](https://github.com/scrapy-plugins/scrapy-splash)  for more information.

## Usage
To scrape countries historic population
```
scrapy crawl countries -o population.csv
```

To scrape covid 19 data
```
scrapy crawl covid19_case -o covid.csv
```


