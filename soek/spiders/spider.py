import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import re
import urlparse
from soek.items import soekItem
import soek.setlog

logger = soek.setlog.logger


class Spider(scrapy.Spider):
    name = "soek"
    allowed_domains = ["iitg.ernet.in"]
    start_urls = [
        "http://intranet.iitg.ernet.in",
        "http://local.iitg.ernet.in"
    ]
    crawledLinks = set()

    def parse(self, response):
        if response.status == 200:
            Spider.crawledLinks.add(response.url)
            logger.debug(response.url)

        hxs = HtmlXPathSelector(response)
        links = hxs.select("//a/@href").extract()

        for link in links:
            _link = self.abs_url(link, response)
            # If it is a proper link and is not checked yet, yield it to the Spider
            if _link not in Spider.crawledLinks:
                yield Request(_link, self.parse)

    def abs_url(self, url, response):
        base = response.xpath('//head/base/@href').extract()
        if base:
            base = base[0]
        else:
            base = response.url
        return urlparse.urljoin(base, url)
