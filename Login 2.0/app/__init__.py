from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Cria Aplicação
app = Flask(__name__)
# Configura Aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
# Cria Database
db = SQLAlchemy(app)
#db.init_app(app)
# Ativa Migrate
Migrate(app, db)

from app import views, models, forms