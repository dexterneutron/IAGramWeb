from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.iagram
#collection = db.iagram
collection = db.iagram_weekly
outputCollection=db.iagram_output


def InsertOutput(quoteid,background,filter,output):
    image = { "quote": quoteid, "background":background,"outputFile":output  }
    x = outputCollection.insert_one(image)

def GetFinalImages():
    ilist=outputCollection.find({})
    return ilist

def DeleteAllOutput():
    ilist=outputCollection.remove({})


def RamdomQuote():
    #q = collection.find(query)
    q=collection.aggregate([{ "$sample": { "size": 1 }}])
    for q in q:
        frase=(q['Frase'])
        autor=(q['Autor'])
    return frase,autor


def GetQuotesList():
    false=False
    #query='"$or":[{"Publicado" : {"$exists":False},"Publicado":{"$not":True}}]'
    q=collection.find({"$or":[{"Publicado" : False,"Publicado":""}]})
    #q=collection.find({})
    return q

def QuotebyId(id):
    q=collection.find_one({"_id": ObjectId(id)})
    frase=(q['Frase'])
    autor=(q['Autor'])
    return frase,autor


""" 
q=GetQuotesList()
for q in q:
        frase=(q['Frase'])
        autor=(q['Autor'])
        print (frase)
        print (autor)


frase,autor=RamdomQuote()   
 """