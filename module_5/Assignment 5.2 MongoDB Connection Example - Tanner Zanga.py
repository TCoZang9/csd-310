# MongoDB Connection Example

# Import MongoClient
from pymongo import MongoClient

# URL Variable
url = "mongodb+srv://admin:admin@cluster0.t7h5jtp.mongodb.net/pytech?retryWrites=true&w=majority"

#Client Variable
client = MongoClient(url)

#DB Variable
db = client.pytech

print(db.list_collection_names)