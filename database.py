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

def createUser(user):
    user1 = validateUser(user['username'])
    if user1:
        return user1
    else:
        return mongo.db.USERS.insert_one(user)