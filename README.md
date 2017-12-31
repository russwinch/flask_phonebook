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
**/contact/++id++**  
GET with  ++id++ of the target contact  

*curl -X GET http://127.0.0.1:5000/contact/1*

### amend contact
**/contact/++id++**  
{"name":"++contact-name++", "phone":"++contact-phone++"}  
PUT and replace ++contact-name++ and ++contact-phone++ with the new data
and ++id++ of the target contact

*curl -d '{"name":"test friend 2","phone":"01234555555"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/contact/1*

### delete contact
**/contact/++id++**  
DELETE with ++id++ of the target contact  

*curl -X DELETE http://127.0.0.1:5000/contact/1*

### selecting environmental configuration
export FLASK_CONFIG=development
export FLASK_CONFIG=production
---

## approach
1. started with [Build Simple Restful Api With Python and Flask Part 2](https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12)
2. broke code down into __init__ and models
3. fixed bug with the add_contact function not returning json
4. adapted script to purpose the fields needed and regenerated db
5. implemented environmental config file and switching. based on [Build a CRUD Web App With Python and Flask - Part One](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)
6. set up manage.py and moved create_db functionality in here
7. created a docker container: rwinch/phonebook:v1
launch locally with *docker run -p 5000:5000 rwinch/phonebook:v1*
8. docker-compose.yml file available. to run as a load balanced service:
- docker swarm init
- docker stack deploy -c docker-compose.yml phonebook

## to do
- authentication: http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/
- implement groups: groups table and link table to assign
- *persist the database so the docker implementation is useful*
- aggregate id column to determine max(id), for testing
- create test scripts
- improve error handling
