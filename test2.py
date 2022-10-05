import pymongo

client = pymongo.MongoClient("mongodb+srv://Mosharrafa:HDj3xJJLwH235jCzQ@cluster0.dbzzgfx.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["food"]

#record = collection.find()

#for i in record:
#    print(i)

#data = collection.find({"product":"Affordable AI"})
data = collection.find({"courseOffered":{"$gt":"E"}})

for i in data:
    print(i)
