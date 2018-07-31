from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # this is the name of the module
# /// means sqlite fille will be saved in same directory *
app.config['SECRET_KEY'] = '1f97f91cfded7cfb92a9fcef1b36db91'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # /// *
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'  # 'info is a blue-colored alert in bootstrap'

from flaskblog import routes
