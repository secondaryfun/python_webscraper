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

# Build a Spider
##### Docs:  https://docs.scrapy.org/en/latest/topics/spiders.html  

## In your spider.py file:

### Response Object:

#### Properties
* response.url
#### Selectors
* response.css 
* response.xpath

## Steps to build a spider:
1. **Enter allowed domain.**
```python
allowed_domains = ['succubuspublishing.com/']
```
2. **Add start_urls:**
```python
start_urls = [
        'http://succubuspublishing.com/um1ch1sparknotes/']
```
3. **Use selector to pull nodes from page. Using Chrome Dev Tools helps to identify the correct selector.**
* xpath:  
```python 
resonse.xpath("//div[@class='my_class']")
```
* Note: xpath class selector must match the exact class list in the html. To search for single class, use:
```python
response.xpath(".//div[contains(concat(' ',normalize-space(@class),' '),' class_name')])
```
* css:
```python
response.css('.class_name::text')
```
* Use .extract() OR to convert the nodes into a list of strings.
* Use .extract_first() to convert the first search result into a string. 
4. **Run for loop to extract individual fields:**
```python
for entry in all_the_faq_divs:
    title = entry.css('.arconix-faq-accordion-title::text').extract_first()
    content = entry.xpath(".//li/text()").extract()
```
5. **To export the extracted fields, use "yield{}"**
```python
yield {
    'title': title,
    'content': content
}
```


## How to run a spider

1. For testing:
```
scrapy crawl spider_name
```
2. To output to file:
```
scrapy crawl spider_name -o filename.json
```