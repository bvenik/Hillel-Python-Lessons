from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

collection.insert_one({'name': 'Max', 'lastname': 'Chefranov', 'age': 30})
collection.insert_one({'country': 'Ukraine', 'city': 'Odessa', 'post_index': 65000})

for document in collection.find():
    print(document)

collection.update_one({'name': 'Max'}, {'$set': {'age': 28}})
collection.delete_many({'name': 'Max'})
print(collection.find())