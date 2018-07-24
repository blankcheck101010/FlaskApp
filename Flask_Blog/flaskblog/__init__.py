from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # this is the name of the module
# /// means sqlite fille will be saved in same directory *
app.config['SECRET_KEY'] = '1f97f91cfded7cfb92a9fcef1b36db91'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # /// *
db = SQLAlchemy(app)

from flaskblog import routes
