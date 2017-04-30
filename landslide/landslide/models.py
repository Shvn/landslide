from pymongo import MongoClient

#get the mongoclient
mongo = MongoClient()

#select database
db = mongo.landslide


class Data(object):

    def __init__(self, continentcode, countrycode, countryname, fatalities, hazard_type, injuries,
    landslide_size, landslide_type, latitude, longitude, storm_name, trigger, tstamp):
        self.continentcode = continentcode
        self.countrycode = countrycode
        self.countryname = countryname
        self.fatalities = fatalities
        self.hazard_type = hazard_type
        self.injuries = injuries
        self. landslide_size = landslide_size
        self.landslide_type = landslide_type
        self.latitude = latitude
        self.longitude = longitude
        self.storm_name = storm_name
        self.trigger = trigger
        self.tstamp = tstamp

    @classmethod
    def getAll(cls):
        return ""

    @classmethod
    def insertDataset(cls, continentcode, countrycode, countryname, fatalities, hazard_type,
    injuries, landslide_size, landslide_type, latitude, longitude, storm_name, trigger, tstamp):
        data = Data(continentcode, countrycode, countryname, fatalities, hazard_type, injuries, landslide_size, landslide_type, latitude, longitude, storm_name, trigger, tstamp)
        id = str(db.DataSet.insert_one(data.__dict__).inserted_id)
