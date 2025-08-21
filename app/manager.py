from coniction import DAL_mongo
import DAL
import os


class Manager:
    def __init__(self):
        self.HOST = os.getenv("HOST", "iranmaldb.gurutam.mongodb.net/")
        self.USER = os.getenv("USER", "IRGC")
        self.PASSWORD = os.getenv("PASSWORD", "iraniraniran")
        self.DB = os.getenv("DATABASE", "IranMalDB")
        self.COLLECTION = os.getenv("COLLECTION", "tweets")
        self.dal=None


        #פונקציית חיבור לדאטא בייס
    def coonect(self):
        try:
            self.dal = DAL_mongo(self.HOST, self.DB, self.COLLECTION, self.USER, self.PASSWORD)
            return self.dal.open_connection()
        except Exception as e:
            return e

    def close_connection(self):
        return self.dal.close_connection()


    def get_all_tweetss(self):
        # try:
        a=self.dal.get_all_tweetss()
        for i in a:
            print(i)

        # except Exception as e:
        #     return e

mm=Manager()
print(mm.coonect())
print(mm.get_all_tweetss())