from notejam import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")
POSTGRES_PORT = get_env_variable("POSTGRES_PORT")

DB_URL = 'postgresql://{user}:{pw}@{url}:{port}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,port=POSTGRES_PORT,db=POSTGRES_DB)
# print(DB_URL)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy()
db.init_app(app)
db.create_all(app)
