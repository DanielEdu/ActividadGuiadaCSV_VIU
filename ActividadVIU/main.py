'''

                     Actividad Guiada 2.
                   CSV Reading with Python 
                         
'''
import csv
import pymongo

csvFileName = 'cars.csv' 

dbStringConnection = "mongodb+srv://user01:user01@cluster0-ss0ab.mongodb.net/test?retryWrites=true"
dbName = 'cars_db'
dbCollection = 'cars' 


def simpleCsvRead():
    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print (row)
            print(row['Model'], row['Year'])
            
    
def csvReadAndInsertIntoMongoDB():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]
    cars.drop()
    
    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        #for row in reader:
            #print (row)
            # print(row['Model'], row['Year'])
        
        cars.insert_many(reader)


def readCarsModels():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]
    
    #for car in cars.find():
    #    print(car)
    
    for car in cars.find({}, { "_id": 1, "Model": 1, "Year": 1 }):
        print(car)


def queryCarModel(carModel):
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]

    print("\nCars of model \'"+carModel+"\' sorted by year\n\n")
    
    myquery = { "Model": { "$regex": ".*" + carModel + ".*" }}
    for car in cars.find(myquery).sort("Year", -1):
        print(car) 


def main():
    #simpleCsvRead()
    csvReadAndInsertIntoMongoDB()    
    #readCarsModels()
    #queryCarModel('ford mustang')

    
main();
