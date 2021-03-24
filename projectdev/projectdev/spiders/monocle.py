# https://monocle.com/travel/athens/hotels/
import scrapy
import json
class Monocle(scrapy.Spider):
    name = "monocle"

    start_urls=['https://monocle.com/travel/athens/hotels/']

    def parse(self,response):
        article_title = response.css('h2.article-subheading::text').extract()[0][0:19]
        article_image = None
        article_summary = None
        article_lang = response.css('html').xpath('@lang').extract()[0]
        article_status = "LOW"
        article_date = None
        hotel_id = "25452876"
        
        # # #outs json, json file can be used in different APIs
        outs = {}
        outs["article_title"]=article_title
        outs["article_image"]=article_image
        outs["article_summary"]=article_summary
        outs["article_lang"]=article_lang
        outs["article_status"]=article_status
        outs["article_date"]=article_date
        outs["hotel_id"]=hotel_id
        
        with open('monocle.json','w') as fp:
            json.dump(outs, fp)
        yield {'outs':outs}
        # yield {'title':article_title}