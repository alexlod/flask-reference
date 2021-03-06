import pytest

from fref import create_app
from fref.models import db

@pytest.fixture
def app():
  app = create_app()
  app.app_context().push()
  db.init_app(app)

  with app.app_context():
    db.create_all()
  
  yield app
  with app.app_context():
    db.session.remove()
    db.drop_all()

@pytest.fixture
def client(app):
  return app.test_client()