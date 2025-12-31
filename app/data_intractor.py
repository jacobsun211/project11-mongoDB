import mysql.connector
import uvicorn
from pymongo import MongoClient

MONGO_URI="mongodb://localhost:27018"
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
            contact = collection.find_one({"_id": id}, 
                        {
                           "first_name": contact.first_name,
                           "last_name": contact.last_name,
                           "phone_number": contact.phone_number
                        })
            return contact
        except:
            return False

    @staticmethod
    def delete_contact(id):  
        try:
            collection.find_one_and_delete({"_id": id})
            return True
        except Exception as e:
            return " error occurred while trying to delete contact:", e
            


# class Contacts:
        

#     @staticmethod
#     def sql_to_dict(rows):
#         contacts_dict = []
#         for contact in rows:
#             row = {"id":contact[0],
#              "first_name":contact[1],
#              "last_name":contact[2],
#              "phone_number":contact[3],
#              }
#             contacts_dict.append(row)
#         return contacts_dict
    
#     @staticmethod
#     def get_all_contacts():
#         cursor.execute("SELECT * FROM contacts")
#         contacts = cursor.fetchall()
#         return contacts

#     @staticmethod
#     def create_contact(first_name, last_name, phone_number):
#         cursor.execute( 
#             f"INSERT INTO contacts (first_name, last_name, phone_number) \
#             VALUES ('{first_name}', '{last_name}', '{phone_number}')")
#         conn.commit()
#         new_id = Contacts.new_contact_id()
#         return new_id
    

#     def new_contact_id():
#         cursor.execute("SELECT MAX(id) FROM contacts;")
#         new_contact_id = cursor.fetchone()
#         return new_contact_id
    
#     @staticmethod
#     def update_contact(id,new_first_name,new_last_name,new_number):  
#         cursor.execute(
#             f"UPDATE contacts \
#             SET first_name = '{new_first_name}', last_name = '{new_last_name}', phone_number = '{new_number}' \
#             WHERE id = '{id}';")
#         conn.commit()
#         return cursor.rowcount > 0

#     @staticmethod
#     def delete_contact(id):
#         cursor.execute(
#             f"DELETE FROM contacts \
#             WHERE id = '{id}';")
#         conn.commit()
#         return cursor.rowcount > 0