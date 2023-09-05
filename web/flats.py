import psycopg2
import pandas as pds
from sqlalchemy import create_engine


def get_flats_from_db():

    alchemyEngine = create_engine('postgresql+psycopg2://docker:Welcome123@vz-db:5432/DBFlats')
    # alchemyEngine = create_engine('postgresql+psycopg2://docker:Welcome123@127.0.0.1:5432/DBFlats')
    dbConnection = alchemyEngine.connect()

    dataFrame = pds.read_sql("select * from flats limit 500", dbConnection)

    dbConnection.close()

    return dataFrame
