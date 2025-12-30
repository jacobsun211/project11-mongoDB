from fastapi import FastAPI
import uvicorn
# from data_intractor import Contacts
from pydantic import BaseModel

app = FastAPI()


class Contact_params(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


@app.get("/contacts")
def get_contacts():
    # contacts = Contacts.get_all_contacts()
    # contacts = Contacts.sql_to_dict(contacts)
    # return contacts
    return "all good"

@app.post("/contacts")
def post_contact(contact: Contact_params):
    new_id = Contacts.create_contact(contact.first_name, contact.last_name, contact.phone_number)
    return {
        "message": "Contact created successfully",
        "id": new_id
        }

@app.put("/contacts{id}")
def update_contact(id, contact: Contact_params):
    bool = Contacts.update_contact(id,contact.first_name, contact.last_name, contact.phone_number)
    return bool


@app.delete("/contacts")
def delete_contact(id: int):
    bool = Contacts.delete_contact(id)
    return bool

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)