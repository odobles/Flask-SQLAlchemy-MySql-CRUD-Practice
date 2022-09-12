from flask import Blueprint, render_template, request, redirect, url_for, flash #flash es una variable que puede ser compartida entre paginas
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST", "PUT"])
def add_contact():
    fullname =request.form["fullname"]
    email =request.form["email"]
    phone =request.form["phone"]
    
    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact was succesfully added")

    # print(new_contact)

    return redirect(url_for('contacts.home'))


@contacts.route("/update/<id>", methods=['GET', 'POST'])
def update_contact(id):

    if request.method == "POST":

        contact = Contact.query.get(id) #Consulte contacto a traves del id
        contact.fullname =request.form["fullname"]
        contact.email =request.form["email"]
        contact.phone =request.form["phone"]

        db.session.commit()
        flash("Contact was succesfully updated")

        return redirect(url_for('contacts.home'))

    contact = Contact.query.get(id)
    return render_template('update.html',contact=contact)

@contacts.route("/delete/<id>")
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash("Contact was succesfully deleted")


    return redirect(url_for('contacts.home'))


@contacts.route("/about")
def about():
    return render_template("about.html")
