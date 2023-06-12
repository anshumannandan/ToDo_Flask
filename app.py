from flask import Flask
import os, dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_rest_paginate import Pagination


dotenv.load_dotenv()
DEBUG = os.environ.get('DEBUG', bool)
DATABASE = os.environ.get('DATABASE')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['PAGINATE_PAGE_SIZE'] = 5

db = SQLAlchemy(app)
ma = Marshmallow(app)
pagination = Pagination(app, db)

from api import *

if __name__ == '__main__':
    app.run(debug=DEBUG)