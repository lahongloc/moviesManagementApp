from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'ASGEY&%^BDFVARQ^SFS'
app.config["SQLALCHEMY_DATABASE_URI"] = str.format("mysql+pymysql://root:{}@localhost/cinemaapp?charset=utf8mb4",
                                                   "Omc6789#")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=app)
login = LoginManager(app=app)

app.config['PAGE_SIZE'] = 8
