from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
db=client['seat']
collection=db['member']
set_num='10411'
set_id='alswns0207'
set_name='박민준'

# result=collection.find_one({'class_num':set_num})
# if result==None:
#     print('있는정보입니다 다시입력해주십시오')
# else:
#     print('성공')
if collection.find_one({'class_num': set_num}) == None:
    print('성공')
else:
    print('있는정보입니다 다시입력해주십시오')