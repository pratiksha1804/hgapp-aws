from config import mongo

def validateUser(username,password):
    data = mongo.db.USER.find_one({"username":username,"password":password}, {'_id': False})
    if data:
        return data
    return None