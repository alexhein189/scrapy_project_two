import scrapy
import json
class Edition(scrapy.Spider):
    name = "edition"

    start_urls=['https://edition.cnn.com/travel/article/best-luxury-seaside-hotels-greece/index.html/']

    def parse(self,response):
        article_title = response.css('title::text').extract()[0] #it will give a list of titles
        article_image = response.css('div.CaptionedImage__cta div img.Image__image').xpath("@src").extract()[-2]
        article_summary = response.css('div.Paragraph__component span::text').extract()[-13]
        article_lang = response.css('html').xpath("@lang").extract()[0]
        article_status = "HIGH"
        article_date = response.css('div.Article__subtitle::text').extract()[-1][10::]
        hotel_id = "25452876"
        
        #outs json, json file can be used in different APIs
        outs = {}
        outs["article_title"]=article_title
        outs["article_image"]=article_image
        outs["article_summary"]=article_summary
        outs["article_lang"]=article_lang
        outs["article_status"]=article_status
        outs["article_date"]=article_date
        outs["hotel_id"]=hotel_id
        
        with open('edition.json','w') as fp:
            json.dump(outs, fp)
        yield {'outs':outs}
        
        
        
        
        # yield {'date':article_date}
        
        
        