import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#Exemplo 1

x = "John"
myquery = {"name" : x}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

#Exemplo 2
myquery = {"name": {"$regex":"^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)


