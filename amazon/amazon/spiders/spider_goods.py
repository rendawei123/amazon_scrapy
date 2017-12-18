# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib.parse import urlencode
from amazon.items import AmazonItem


class SpiderGoodsSpider(scrapy.Spider):
    name = 'spider_goods'  # 爬虫名字
    allowed_domains = ['www.amazon.cn']  # 限制只能从这个网站爬取数据
    # start_urls = ['http://www.amazon.cn/']   # 起始页面的地址，我们爬取网站都是不固定的

    def __init__(self, keyword=None, *args, **kwargs):
        super(SpiderGoodsSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword

    # 此方法是用来定义爬虫起始页面的地址
    def start_requests(self):
        url = 'https://www.amazon.cn/s/ref=nb_sb_noss_2?'   # 起始页面地址
        # 搜索项
        parmas = {
            'field-keywords': self.keyword
        }
        # 拼接地址
        url = url + urlencode(parmas, encoding='utf-8')

        # 提交请求,必须要用yield提交注意给request 传入回调函数,一旦返回结果就会传给回调函数
        yield Request(url, callback=self.parse_index)

    def parse_index(self, response):
        # 使用xpath选取商品详情信息的链接
        urls = response.xpath('//*[contains(@id,"result_")]/div/div[3]/div[1]/a/@href').extract()
        # print('--------', urls)
        # 拿到所有的url之后就要挨个给每个url发请求
        for url in urls:
            yield Request(url, callback=self.parse_detail)  # 请求详情页

        # 拿到下一页的url,并且自动拼接成正确的路径
        next_url = response.urljoin(response.xpath('//*[@id="pagnNextString"]/@href').extract())
        # 继续给下一页发送请求，回调函数还是它自己
        yield Request(next_url, callback=self.parse_index)

    def parse_detail(self, response):
        # 编辑items.py
        # 导入AmazonItem类
        # 实例化item=AmazonItem()
        # print('-------详情页', response.url)
        item = AmazonItem()
        item['goods_name'] = response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
        item['goods_price'] = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first().strip()
        # item['goods_price']=
        # item['delivery_mod']=
        # 解析response.text的内容，拿到商品名，价钱，快递方式
        return item
# 切换到项目目录下命令行运行爬虫，需要传入搜索关键词
# scrapy crawl spider_goods -a keywords=iphone
# 执行这条命名首先会找到spider_goods这个文件，然后实例化里面的类，然后将参数传给类里面的__init__函数
