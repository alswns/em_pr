from pymongo import MongoClient
client = MongoClient()
# 클래스 객체 할당

client = MongoClient('localhost', 27017)
db=client['seat']
collection=db['seat']
result=collection.find({'name':'제1강의실'})
for i in result:
    seat=i['seat']
seat=list(seat)
print(seat)