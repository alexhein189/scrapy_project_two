# https://www.cntraveler.com/hotels/greece/mykonos/mykonos-blu
import scrapy
import json
class Cntravelerkudos(scrapy.Spider):
    name = "cntravelerkudos"

    start_urls=['https://www.cntraveller.com/article/travel-guide-mykonos']

    def parse(self,response):
        article_title = response.css('h1.a-header__title::text').extract()[0]
        article_image = None
        article_summary = response.css('p.bb-p::text').extract()[12][3::].split(".")[0]
        article_lang = response.css('html').xpath('@lang').extract()[0]
        article_status = "MEDIUM"
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
        
        with open('cntravelerkudos.json','w') as fp:
            json.dump(outs, fp)
        yield {'outs':outs}
        # yield {'summary':article_summary}