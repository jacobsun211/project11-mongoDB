import mysql.connector
import uvicorn
from pymongo import MongoClient
import os


db_uri = os.getenv("MONGO_HOST")
MONGO_URI=F"mongodb://{db_uri}:27018"
DB_NAME="mongoDB"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["contacts"]

class Contacts:

    @staticmethod
    def get_contacts():
        try:     
            contacts = collection.find()
            return contacts
        except Exception as e:
            return " error occurred while testing MongoDB connection:", e
            


    @staticmethod
    def create_contact(contact):
        highest_id = collection.find_one(sort=[("_id", -1)])
        new_id = highest_id["_id"] + 1
        new_contact = {
             "_id": new_id,
            "first_name": contact.first_name,
            "last_name": contact.last_name,
            "phone_number": contact.phone_number
        }
        collection.insert_one(new_contact)
        return new_id


    @staticmethod
    def update_contact(id,contact):  
        try:
            collection.find_one({"_id": id}, 
                        {
                           "first_name": contact.first_name,
                           "last_name": contact.last_name,
                           "phone_number": contact.phone_number
                        })
            return True
        except:
            return False

    @staticmethod
    def delete_contact(id):  
        try:
            collection.find_one_and_delete({"_id": id})
            return True
        except Exception as e:
            return " error occurred while trying to delete contact:", e
            

