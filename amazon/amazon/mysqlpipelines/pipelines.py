# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sql import Sql


class AmazonPipeline(object):
    def process_item(self, item, spider):
        name = item['goods_name']
        price = item['goods_price']
        print(name, price)

        if not Sql.is_repeat(name, price):
            Sql.insert_table_goods(name, price)
