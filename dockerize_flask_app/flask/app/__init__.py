from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

db = SQLAlchemy()
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

from app import views