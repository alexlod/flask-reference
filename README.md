A refernce Flask application with common modules such as SQLAlchemy.

Project was created from https://dev.to/therealdarkmage/creating-a-new-flask-project-with-pipenv-i93

To run the application:
```
pipenv shell
flask run
```

To run tests:
```
pipenv shell
python -m pytest
```

Other modules this reference could incorporate:

 * OpenAPI documentation with apispec and Swagger (swagger-ui) for API documentation and experimentation
 * Marshmallow for API JSON validation and serializing JSON to Python, possibly integrated with SQLAlchemy for database-level validation as well
 * Flask-RESTful
 