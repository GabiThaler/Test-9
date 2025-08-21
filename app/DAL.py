from pymongo import MongoClient



class DAL:
    # חיבור למסד
    def __init__(self):
        self.client = MongoClient("mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
        self.db = self.client["IranMalDB"]
        self.collection = self.db["tweets"]
    #
        self.documents = self.collection.find()

    # מעבר על המסמכים והדפסה
    def print_all_data(self):
        for doc in self.documents:
            print(doc)

        return self.documents

