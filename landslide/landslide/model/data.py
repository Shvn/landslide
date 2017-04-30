class Data(object):
    """description of class"""
    def __init__(self, id):
        self.id = id

    @classmethod
    def find_by_id(cls, id):
        result = {}
        #query db for data of particular id
        return result

    @classmethod
    def find_all(cls):
        result = {}
        #query db for all data
        return result
