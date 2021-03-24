import scrapy
import json
class Escape(scrapy.Spider):
    name = "escape"

    start_urls=['https://www.escape.com.au/top-lists/18-places-for-romance/image-gallery/af994cfff4f5f11713353170edbccd9e']

    def parse(self,response):
        article_title = response.css('div.gallery-meta h1::text').extract()[0]
        article_image = response.css('div.gallery-slide img').xpath('@src').extract()[3]
        article_summary = response.css('div.slide-descripton::text').extract()[8]
        article_lang = response.css('html').xpath('@lang').extract()[0]
        article_status = "MEDIUM"
        article_date = None
        hotel_id = "25452876"
        
        # #outs json, json file can be used in different APIs
        outs = {}
        outs["article_title"]=article_title
        outs["article_image"]=article_image
        outs["article_summary"]=article_summary
        outs["article_lang"]=article_lang
        outs["article_status"]=article_status
        outs["article_date"]=article_date
        outs["hotel_id"]=hotel_id
        
        with open('escape.json','w') as fp:
            json.dump(outs, fp)
        yield {'outs':outs}
        
        

# name = "Escape"

#     start_urls=['https://www.escape.com.au/top-lists/18-places-for-romance/image-gallery/af994cfff4f5f11713353170edbccd9e']

#     def parse(self,response):
#         article_title = 
#         article_image = 
#         article_summary = 
#         article_lang = 
#         article_status = 
#         article_date = 
#         hotel_id = 
        
#         #outs json, json file can be used in different APIs
#         outs = {}
#         outs["article_title"]=article_title
#         outs["article_image"]=article_image
#         outs["article_summary"]=article_summary
#         outs["article_lang"]=article_lang
#         outs["article_status"]=article_status
#         outs["article_date"]=article_date
#         outs["hotel_id"]=hotel_id
        
#         with open('.json','w') as fp:
#             json.dump(outs, fp)
#         yield {'outs':outs}
        
        
# count  = 0
# for article in article_summary:
#     count += 1
#     if 'Whitewashed' in article.split(" "):
#         yield {'hell_count':count}