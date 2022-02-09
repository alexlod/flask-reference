import os

from flask import Flask

def create_app():
  app = Flask(__name__, instance_relative_config=True)

  class Config(object):
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = True # set to False in production
    TESTING = True # set to False when running not in tests
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  app.config.from_object(Config())

  from fref import models
  models.init_app(app)

  from fref import hello
  hello.init_app(app)

  return app