# python_webscraper

## Steps to Install

1. Create the python project environment

```
pipenv shell
```

2. Install dependencies
```
pip install scrapy

pip freeze // check the dependencies
```

3. Create a scrapy project
```
scrapy startproject project_name
```
4. Cd into project_name folder
5. Create a spider
```
scrapy genspider spider_name url  //  example:  scrapy genspider spider succubuspublishing.com/downloads
```

## Build a Spider

### In your spider.py file:
*. Response Object:
* response.url
* response.css
* response.xpath

## How to run a spider

1. For testing:
``` 
scrapy crawl spider_name
```
2. To output to file:
```
scrapy crawl spider_name -o filename.json
```