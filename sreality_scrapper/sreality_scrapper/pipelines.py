# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2
from sqlalchemy import create_engine


import psycopg2

class SrealityScrapperPipeline:

    def __init__(self):
        alchemyEngine = create_engine('postgresql+psycopg2://docker:Welcome123@vz-db:5432/DBFlats')
        # alchemyEngine = create_engine('postgresql+psycopg2://docker:Welcome123@127.0.0.1:5432/DBFlats')
        self.connection = alchemyEngine.connect()

        ## Create cursor, used to execute commands
        self.connection = alchemyEngine.raw_connection()
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):

        # Check to see if text is already in database

        self.cur.execute("select * from public.flats where imageurl = %s and title = %s", (item["imageurl"], item["title"]))
        result = self.cur.fetchone()

        # If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item["imageurl"])

        # If text isn't in the DB, insert data
        else:
            ## Define insert statement
            self.cur.execute("""insert into public.flats (title, imageurl) values (%s,%s)""", (
            item["title"],
            item["imageurl"]
            ))
            self.connection.commit()

        return item


    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()