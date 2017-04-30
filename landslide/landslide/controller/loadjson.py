from model.data import Data
import json
import dateutil.parser

class LoadJson:
    def __init__(self):
        self.read()
    def read(self):
        with open('dataset.json') as data_file:
            data = json.load(data_file)
            for x in data:
                if 'continentcode' in x:
                    continentcode = x["continentcode"]
                else:
                    continentcode = ''
                if 'countrycode' in x:
                    countrycode = x["countrycode"]
                else:
                    countrycode = ''
                if 'countryname' in x:
                    countryname = x["countryname"]
                else:
                    countryname = ''
                if 'fatalities' in x:
                    fatalities = int(x["fatalities"])
                else:
                    fatalities = 0
                if 'hazard_type' in x:
                    hazard_type = x["hazard_type"]
                else:
                    hazard_type = ''
                if 'injuries' in x:
                    injuries = int(x["injuries"])
                else:
                    injuries = 0
                if 'landslide_size' in x:
                    landslide_size = x["landslide_size"]
                else:
                    landslide_size = ''
                if 'landslide_type' in x:
                    landslide_type = x["landslide_type"]
                else:
                    landslide_type = ''
                if 'latitude' in x:
                    latitude = float(x["latitude"])
                if 'longitude' in x:
                    longitude = float(x["longitude"])
                if 'storm_name' in x:
                    storm_name = x["storm_name"]
                else:
                    storm_name = ''
                if 'trigger' in x:
                    trigger = x["trigger"]
                else:
                    trigger = ''
                if 'tstamp' in x:
                    tstamp = dateutil.parser.parse(x["tstamp"])
                else:
                    tstamp = ''
                Data.insertDataset(continentcode, countrycode, countryname, fatalities, hazard_type,
                injuries, landslide_size, landslide_type, latitude, longitude, storm_name, trigger, tstamp)
x = LoadJson()
