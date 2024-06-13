from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://std_2588_exam_library:1324354657@std-mysql.ist.mospolytech.ru/std_2588_exam_library' # "sqlite:///F:/work/artem2/instance/nusers.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



from reader import routes, models