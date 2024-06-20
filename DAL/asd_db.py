
from pymongo import MongoClient
from bson import ObjectId

class AsdDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["tests"]
        self.__collection_tests = self.__db["asd_tests"]
        


    def insert_new_tests(self,testObj):
        try:
            self.__collection_tests.insert_one(testObj)
            return [{"Success":"created with id: {}".format(str(testObj["_id"]))}]
        except Exception as e:
            return [{"Error":"An error occurred"}]
    