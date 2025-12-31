# please read me! (.md)

## author:
# Jacob shemesh
# 325606481
# negev

copyright disclaimer: if you want to copy this code... be my guest, i dont know waht you found here tbh...




# what i maneged to do

i did Docker, sql database, api application
each one with branch of his own 

all endpoints work
(except PUT which works in sql query but i didnt sure on how to do it in the endpoints)



## how to run the code ##

```bash
docker compose up --build 
```

then open: (optional)
http://localhost:8000/docs  



in postman:

url: (http://localhost:8000/contacts/)

POST endpoint:

write this format in body:
{
    "first_name":"x",
    "last_name": "y",
     "phone_number":"010110101"
}

returns:
  {
     "message": "Contact created successfully",
     "id": new_id
        }


DELETE endpoint:

http://localhost:8000/contacts/?id=1 (the id of the contact you want to delete)

returns: True or False

