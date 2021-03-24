# https://www.cntraveler.com/hotels/greece/mykonos/mykonos-blu
import scrapy
import json
class Cntraveler(scrapy.Spider):
    name = "cntraveler"

    start_urls=['https://www.cntraveler.com/hotels/greece/mykonos/mykonos-blu']

    def parse(self,response):
        article_title = response.css('h1.content-header__row::text').extract()[0]
        article_image = response.css('picture.lead-asset__media img').xpath('@src').extract()[0]
        article_summary = None
        article_lang = response.css('html').xpath('@lang').extract()[0]
        article_status = "MEDIUM"
        article_date = "2019"
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
        
        with open('cntraveler.json','w') as fp:
            json.dump(outs, fp)
        yield {'outs':outs}
        #yield {'summary':article_summary}