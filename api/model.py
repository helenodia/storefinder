import json


class Store:
    """
     A class used to represent a Store

     Attributes
     ----------
     name : str
         the name of the town or city where the store is located
     postcode : str
         the store's postcode
     """
    def __init__(self, name, postcode):
        self.name = name
        self.postcode = postcode


storesData = []

with open('./static/stores.json', 'r') as f:
    storesData = json.load(f)


def get_stores_data():
    """Returns static stores data (list of dicts) until/if I add a database"""
    return storesData
