from pymongo import MongoClient

def get_databse(db):
    CONN_STR = 'mongodb://127.0.0.1:27017'
    client = MongoClient(CONN_STR)

    return client[db]