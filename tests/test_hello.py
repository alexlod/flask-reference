import pytest

from fref.models import Foo

def test_root(client):
  response = client.get('/')
  assert response.status_code == 200
  assert response.json == {'message': 'Hello, World!'}
  assert len(Foo.query.all()) == 1