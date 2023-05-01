import random
import string
import pymongo
import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['codes']
def generate_code(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

code = generate_code(10)
print(code)

today = datetime.datetime.now()
code_dict = {"code": code, "date": today}
result = collection.insert_one(code_dict)
print(result.inserted_id)