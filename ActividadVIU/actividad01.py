
'''

                     Actividad  2.1
                   CSV,JSON,XML Reading/Write with Python 
                         
'''
import csv
import json
import pymongo
import urllib
import dicttoxml 
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET

###################################################


csvFileName = 'cars.csv'
jsonFileName = 'cars.json'
xmlFileName = 'cars.xml'

#datos de conexión a mongodb
dbStringConnection = "mongodb+srv://daniel:root@pymongodb-dhkxn.mongodb.net/test?retryWrites=true"
dbName = 'cars_db_json'
dbCollection = 'cars'

#From csv to Json
def createJsonFromCsv():
    csvfile = open(csvFileName, 'r')
    jsonfile = open(jsonFileName, 'w')

    reader = csv.DictReader( csvfile)
    title = reader.fieldnames
    csv_rows=[] 

    for row in reader:
        csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])

    js = json.dumps(csv_rows, indent=2)
    jsonfile.write(js)
    print('done')


#read Json and writw into mongodb
def readJson(jsonFile):
    with open(jsonFile) as j_file:  
        data = json.load(j_file)
    
    return data


#insert into MongoDb  
def insertIntoMongo(data):
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]
    cars.drop()
    cars.insert_many(data)
    print('done')


#busqueda en Mongodb
def queryCarModel():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]
    json_rows=[]

    for car in cars.find({}, { "_id": 0, "Model": 1, "Horsepower": 1, "Accelerate":1 }).sort("Horsepower",1):
        json_rows.append(car)

    js = json.dumps(json_rows, indent=2)
    jsonfile = open(jsonFileName, 'w')
    jsonfile.write(js)
    print('done')
        

#From Json to XML, save_file .xml
def jsonToXml():
    with open(jsonFileName) as json_file:  
        data = json.load(json_file)  

    xml = dicttoxml.dicttoxml(data)
    dom = parseString(xml).toprettyxml()
    myfile = open(xmlFileName, "w")  
    myfile.write(dom) 
    print('done') 




if __name__ == "__main__":
    #createJsonFromCsv()
    #data = readJson(jsonFileName)
    #insertIntoMongo(data)
    #queryCarModel()
    jsonToXml()