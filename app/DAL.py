from pymongo import MongoClient

# חיבור למסד
client = MongoClient("mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
db = client["IranMalDB"]
collection = db["tweets"]

documents = collection.find()

# מעבר על המסמכים והדפסה
for doc in documents:
    print(doc)