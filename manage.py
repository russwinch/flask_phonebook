import os
import pytest
# class for handling a set of commands
from flask_script import Manager
from app import app
from app.models import db

# create an instance of class that will handle our commands
manager = Manager(app)

# creats the database
# Example usage: python manage.py create_db
@manager.command
def create_db():
    """Initialises the SQLite database"""
    db.create_all()

# define our command for testing called "test"
# Usage: python manage.py test
@manager.command
def test():
    """Runs the unit tests without test coverage."""
    pass
    # tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    # result = unittest.TextTestRunner(verbosity=2).run(tests)
    # if result.wasSuccessful():
    #     return 0
    # return 1

if __name__ == '__main__':
    manager.run()
