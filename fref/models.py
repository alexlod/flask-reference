from sqlalchemy import Column, Integer
from flask_sqlalchemy import SQLAlchemy

app = None
db = SQLAlchemy()

class Foo(db.Model):
  __tablename__ = 'foos'
  id = Column(Integer, primary_key=True)

def init_app(local_app):
  global app
  app = local_app
  db.init_app(app)

def commit():
  try:
    db.session.commit()
  except:
    db.session.rollback()
    raise