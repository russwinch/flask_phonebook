from flask import request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(15), unique=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'phone')


contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)


# endpoint to create new contact
@app.route("/contact", methods=["POST"])
def add_contact():
    try:
        name = request.json['name']
        phone = request.json['phone']
        new_contact = Contact(name, phone)
        db.session.add(new_contact)
        db.session.commit()

        contact = Contact.query.get(new_contact.id)
        return contact_schema.jsonify(contact)
    except:
        abort(400)

# endpoint to show all contacts
@app.route("/contact", methods=["GET"])
def get_contact():
    all_contacts = Contact.query.all()
    result = contacts_schema.dump(all_contacts)
    return jsonify(result.data)


# endpoint to get contact detail by id
@app.route("/contact/<id>", methods=["GET"])
def contact_detail(id):
    contact = Contact.query.get(id)
    print(contact)
    if not contact:
        abort(404)
    return contact_schema.jsonify(contact)


# endpoint to update contact
@app.route("/contact/<id>", methods=["PUT"])
def contact_update(id):
    try:
        contact = Contact.query.get(id)
        name = request.json['name']
        phone = request.json['phone']

        contact.name = name
        contact.phone = phone

        db.session.commit()
        return contact_schema.jsonify(contact)

    except:
        abort(400)

# endpoint to delete contact
@app.route("/contact/<id>", methods=["DELETE"])
def contact_delete(id):
    try:
        contact = Contact.query.get(id)
        db.session.delete(contact)
        db.session.commit()

        return contact_schema.jsonify(contact)

    except:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
