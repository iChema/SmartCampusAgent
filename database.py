import os
from dotenv import load_dotenv
import pymongo as mongo

load_dotenv()

# Database
cliente = mongo.MongoClient(os.getenv('DATABASE_URI'))
db = cliente[os.getenv('DATABASE_NAME')]

def update_status(id):
    col = db['agent']

    query = { "_id" : id }
    val = { "status" : "online" }

    col.update(query , val , upsert=True)