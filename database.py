from config import mongo
from bson.objectid import ObjectId

def validateUser(username):
    user = mongo.db.USERS.find_one({"username":username}, {'_id': False})
    if user:
        return user
    return None

def getRole(roleid):
    role = mongo.db.ROLES.find_one({"_id":ObjectId(roleid)})
    if role:
        return role
    return None