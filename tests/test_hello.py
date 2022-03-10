import pytest

from fref.models import Foo, FooFactory

def test_root(client):
  response = client.get('/')
  assert response.status_code == 200
  assert response.json == {'message': 'Hello, World!'}
  assert len(Foo.query.all()) == 1

  FooFactory(id=None) # None to let the DB generate the ID
  assert len(Foo.query.all()) == 2