# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class FlipscrapPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://{USR}:{PWD}@cluster0.zma9z.mongodb.net/{DB}?retryWrites=true&w=majority")
        dataBase = self.conn['{DB}']
        self.collection = dataBase['{COLL}']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
        #pass

# {USR} = DB user name
# {PWD} = DB user password 
# {DB} = database name
# {COLL} = collection name