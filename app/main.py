from fastapi import FastAPI
import uvicorn
# from data_intractor import Contacts
from data_intractor import Contacts
from typing import Any
from pydantic import BaseModel

from bson import json_util
import json

app = FastAPI()


class Contact_params(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.get("/contacts")
def get_all_contacts():
    contacts = Contacts.get_contacts()
    return json.loads(json_util.dumps(contacts))

@app.post("/contacts")
def post_contact(contact: Contact_params):
    new_id = Contacts.create_contact(contact)  
    return {
    "message": "Contact created successfully",
    "id": new_id
}
# -------------------------------------------------------
# # to do: make phone number uniqie (pydantic, discord)
# -------------------------------------------------------
    
#     new_id = Contacts.create_contact(contact.first_name, contact.last_name, contact.phone_number)
#     return {
#         "message": "Contact created successfully",
#         "id": new_id
#         }

# @app.put("/contacts{id}")
# def update_contact(id, contact: Contact_params):
#     bool = Contacts.update_contact(id,contact.first_name, contact.last_name, contact.phone_number)
#     return bool


# @app.delete("/contacts")
# def delete_contact(id: int):
#     bool = Contacts.delete_contact(id)
#     return bool



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)