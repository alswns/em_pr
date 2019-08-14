from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db=client['setting']
client.get_database(name='setting')
client.cre
