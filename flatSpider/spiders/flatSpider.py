'''
Created on Oct 6, 2014

@author: Gabor
'''
from scrapy.contrib.spiders.crawl import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector.lxmlsel import HtmlXPathSelector
class flatSpider(CrawlSpider):
    name = "flatSpider"
    start_url =['http://www.bazar.at/wien-wohnungen-anzeigen,dir,1,cId,14,fc,9,loc,9,o,1,ref,4,ret,8,tp,0,at,1922']
    allowed_domains= ['bazar.at']
    rules =(
            Rule(SgmlLinkExtractor(allow=("http://www.bazar.at/wien-wohnungen-anzeigen,dir,1,cId,14,fc,9,loc,9,o,1,ref,4,ret,8,tp,0,at,1922",)),callback ='parse_item'),
          )
    def parse_item(self, response):
        hsx = HtmlXPathSelector(response)
        print response.selector.xpath('//title/text()')