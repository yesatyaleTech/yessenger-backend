import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta

client = pymongo.MongoClient('localhost:27017')

db = client['testDB']
users = db.userCollection

# HELPER FUNCTIONS

def create_user_model():

    first_name = str(input("First Name: "))
    last_name = str(input("Last Name: "))
    phone_number = str(input("Phone Number: "))
    address = str(input("Address: "))
    email = str(input("Email Address: "))

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "name": first_name+" "+last_name,
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "billing_info": [
            {
                "start_date": datetime.utcnow(),
                "end_date": datetime.utcnow() + timedelta(weeks=4),
                "users": set(),
                "message_count": 0
            }
        ]
    }
        
    return user

def get_user_name(user):
    return user['name']

# CRUD FUNCTIONS

def add_user(user):
    users.insert_one(user)

def fetch_all_users():
    return users.find()

def delete_all(): #DONE
    return users.delete_many({})

# Search by full name
def delete_one(name): #DONE
    search = search_user(name)
    if(search):
        users.delete_one(search)
        return True
    return False

# Search by full name
def search_user(name):
    check = None
    for contact in users.find():
        if get_user_name(contact) == name:
            check = contact
    return check
