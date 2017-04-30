from pymongo import MongoClient

#get the mongoclient
mongo = MongoClient()

#select database
db = mongo.radionomics


class Data(object):

    @classmethod
    def getAll(cls):
        return ""
