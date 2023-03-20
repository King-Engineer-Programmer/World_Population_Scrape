# Define your item pipelines here
# Stores the items that you store in the database
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class WorldometersPipeline:
    collection_name="world_data"

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(" ***")
        self.db=self.client["WORLDDATA"]

    def close_spider(self,spider):
        self.client.close()   

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
