from db_connect import connect
import pandas.io.sql as psql
import pandas as pd

def data():

    """ creating the instance to the database and retrieving the sample cropdata stored in the database """

    dbInstance=connect()
    crop_data=psql.read_sql("select * from andhra_crop_details",dbInstance)
    
    return(crop_data)

if __name__=="__main__":
    data()