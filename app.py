from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.contacts import contacts

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:j160920P.@127.0.0.1/contactsdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'

SQLAlchemy(app)



app.register_blueprint(contacts)