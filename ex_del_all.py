import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"name": {"$regex":"^S"}}

x = mycol.delete_many(myquery)
#x = mycol.delete_many({})

print(x.deleted_count, " documentos deletados")
