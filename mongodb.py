import json

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://asutoshdalei:28HZDj2ZOR3mTmPr@experimental.fyt1gps.mongodb.net/?retryWrites=true&w=majority&appName=experimental"

def getDB(uri, dbName='daiTech'):
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client[dbName]

def pushInfo(document, uri=uri):
    daiDb = getDB(uri)
    userEstimatesDoc = daiDb.userEstimates
    userEstimatesDoc.insert_one(document)
