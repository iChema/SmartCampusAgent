import os
from turtle import update
from dotenv import load_dotenv
import pymongo as mongo
from datetime import datetime, timedelta
from bson.json_util import dumps, loads
import json
load_dotenv()

# Database
cliente = mongo.MongoClient(os.getenv('DATABASE_URI'))
db = cliente[os.getenv('DATABASE_NAME')]
agentUpdate = False

def update_status(id):
    col = db['agent']
    query = { "_id" : id }
    val =   { "$set": { "status" : "online" } }
    if col.find_one(query):
        col.update_one(query , val)
    else:
        col.insert_one({ "_id" : id , "status" : "online", "build":"Postgrado", "location":"Laboratorio 1","dates":[]})

def update_sensors(id, sensors):
    agentUpdate = False
    col = db['agent']
    query = { "_id" : id }
    values = col.find_one(query)['dates']
    #print(dates)
    #json_data = dumps(dates, indent = 2)
    if values==[]:
        values=[{
            "date": datetime.now(),
            "co2": sensors[0],
            "co": sensors[1],
            "noise": sensors[2],
            "humidity": sensors[3],
            "temperature_c": sensors[4],
            "temperature_f": sensors[5],
            "heat_index_c": sensors[6],
            "heat_index_f": sensors[7]
        }]
        agentUpdate=True        
    elif values[-1]['date']< datetime.now()-timedelta(seconds=5*60):
        #print(dates[-1]['date'])
        values.append({
            "date": datetime.now(),
            "co2": sensors[0],
            "co": sensors[1],
            "noise": sensors[2],
            "humidity": sensors[3],
            "temperature_c": sensors[4],
            "temperature_f": sensors[5],
            "heat_index_c": sensors[6],
            "heat_index_f": sensors[7]
        })
        agentUpdate=True
    #print(values)
    val = { "$set":  { "dates": values } }    
    if col.find_one(query):
        col.update_one(query , val)
    return agentUpdate