# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2
from psycopg2 import OperationalError
import pandas as pds
from sqlalchemy import create_engine


import psycopg2

class SrealityScrapperPipeline:

    def __init__(self):
        alchemyEngine = create_engine('postgresql+psycopg2://docker:Welcome123@vz-db:5432/DBFlats')
        self.connection = alchemyEngine.connect()

        ## Create cursor, used to execute commands
        self.connection = alchemyEngine.raw_connection()
        self.cur = self.connection.cursor()
        # self.cur = self.connection.cursor()

        # ## Create quotes table if none exists
        # self.cur.execute("""
        # CREATE TABLE IF NOT EXISTS quotes(
        #     id serial PRIMARY KEY,
        #     content text,
        #     tags text,
        #     author VARCHAR(255)
        # )
        # """)

    def process_item(self, item, spider):
        ## Define insert statement
        self.cur.execute(""" insert into public.flats (title, imageurl) values (%s,%s)""", (
            item["title"],
            item["imageurl"]
        ))


        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()