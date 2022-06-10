# File that will run our application
from app import create_app,db 
# Manager class to initialize the extension
# Server class to launch the server
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Blog,Comment

# Creating app instance
app = create_app('production')

manager = Manager(app)
# add_command() method to create 'sever' which will launch the app server
manager.add_command('server',Server)

# migration
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

# For Tests
@manager.command
def test():
    """
    Run the unit tests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# Shell Context
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User,Blog = Blog,Comment = Comment)

if __name__ == '__main__':
    manager.run()