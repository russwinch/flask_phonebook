# phonebook contacts

## functionality
### add a new contact
**/contact**
{"name":"++contact-name++", "phone":"++contact-phone++"}
POST and replace ++contact-name++ and ++contact-phone++ with the incoming data

*curl -d '{"name":"test friend","phone":"01234567891"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/contact*

### show all contacts
**/contact**
GET

*curl -X GET http://127.0.0.1:5000/contact*

### show specific contact
**/contact/<id>**
GET with  <id> of the target contact

*curl -X GET http://127.0.0.1:5000/contact/1*

### amend contact
**/contact/<id>**
{"name":"++contact-name++", "phone":"++contact-phone++"}
PUT and replace ++contact-name++ and ++contact-phone++ with the new data
and <id> of the target contact

*curl -d '{"name":"test friend 2","phone":"01234555555"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/contact/1*

### delete contact
**/contact/<id>**
DELETE with <id> of the target contact

*curl -X DELETE http://127.0.0.1:5000/contact/1*

## approach
1. started with [Build Simple Restful Api With Python and Flask Part 2](https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12)
2. fixed bug with the add_contact function not returning json
3. adapted script to purpose the fields needed and regenerated db

## to do
- authentication: http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/
- implement groups: groups table and link table to assign
- aggregate id column to determine max(id), for testing
