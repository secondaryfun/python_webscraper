import scrapy

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['succubuspublishing.com/']
    start_urls = [
        'http://succubuspublishing.com/um1ch1sparknotes/',
        'http://succubuspublishing.com/um1ch2sparknotes/',
        'http://succubuspublishing.com/um-chapter-3-spark-notes/',
        'http://succubuspublishing.com/um-chapter-4-spark-notes/',
        'http://succubuspublishing.com/um1-chapter-5-spark-notes/',
        ]

    def parse(self, response):
        all_the_faq_divs = response.css('.arconix-faq-accordion-wrap')

        chapter = response.url[36]
        if "-" in response.url:
            chapter = response.url[42]
        if "5" in response.url:
            chapter = response.url[43]
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(chapter)

        for entry in all_the_faq_divs:
            title = entry.css('.arconix-faq-accordion-title::text').extract_first()
            content = entry.xpath(".//div[contains(concat(' ',normalize-space(@class),' '),' arconix-faq-accordion-content')]//li").extract()
            
            yield {
                'chapter': chapter,
                'title': title,
                'content': content
            }