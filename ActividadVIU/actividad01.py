
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

#converti de csv a Json
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


#read Json and writw into mongodb
def readJson():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]
    cars.drop()

    with open(jsonFileName) as json_file:  
        data = json.load(json_file)
    
    cars.insert_many(data)


#busqueda en Mongodb
def queryCarModel():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]

    for car in cars.find({}, { "_id": 0, "Model": 1, "Horsepower": 1, "Accelerate":1 }).sort("Horsepower",1):
        print(car)
        

#convertir de Json a XML, save_file .xml
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
    #readJson()
    #queryCarModel()
    jsonToXml()