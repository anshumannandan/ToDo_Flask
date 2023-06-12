from flask import Flask
import os, dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


dotenv.load_dotenv()
DEBUG = os.environ.get('DEBUG', bool)
DATABASE = os.environ.get('DATABASE', bool)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

db = SQLAlchemy(app)
ma = Marshmallow(app)

from api import *

if __name__ == '__main__':
    app.run(debug=DEBUG)