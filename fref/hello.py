from flask import jsonify

from fref.models import db, commit, Foo

def init_app(app):

  @app.route('/')
  def root():
    foo = Foo()
    db.session.add(foo)
    commit()

    return jsonify({'message': 'Hello, World!'})
