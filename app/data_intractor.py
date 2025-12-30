import mysql.connector
import uvicorn

conn = mysql.connector.connect(
            host="db",
            port=3306,
            user="user",
            password="7618",
            database="db",)
cursor = conn.cursor()

# class Contacts:
        

    # @staticmethod
    # def sql_to_dict(rows):
    #     contacts_dict = []
    #     for contact in rows:
    #         row = {"id":contact[0],
    #          "first_name":contact[1],
    #          "last_name":contact[2],
    #          "phone_number":contact[3],
    #          }
    #         contacts_dict.append(row)
    #     return contacts_dict
    
    # @staticmethod
    # def get_all_contacts():
    #     cursor.execute("SELECT * FROM contacts")
    #     contacts = cursor.fetchall()
    #     return contacts

    # @staticmethod
    # def create_contact(first_name, last_name, phone_number):
    #     cursor.execute( 
    #         f"INSERT INTO contacts (first_name, last_name, phone_number) \
    #         VALUES ('{first_name}', '{last_name}', '{phone_number}')")
    #     conn.commit()
    #     new_id = Contacts.new_contact_id()
    #     return new_id
    

    # def new_contact_id():
    #     cursor.execute("SELECT MAX(id) FROM contacts;")
    #     new_contact_id = cursor.fetchone()
    #     return new_contact_id
    
    # @staticmethod
    # def update_contact(id,new_first_name,new_last_name,new_number):  
    #     cursor.execute(
    #         f"UPDATE contacts \
    #         SET first_name = '{new_first_name}', last_name = '{new_last_name}', phone_number = '{new_number}' \
    #         WHERE id = '{id}';")
    #     conn.commit()
    #     return cursor.rowcount > 0

    # @staticmethod
    # def delete_contact(id):
    #     cursor.execute(
    #         f"DELETE FROM contacts \
    #         WHERE id = '{id}';")
    #     conn.commit()
    #     return cursor.rowcount > 0