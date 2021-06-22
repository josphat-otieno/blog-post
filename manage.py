from app import create_app ,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Quote, User, Post,Comment, Subscribers


app = create_app('production')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    '''
    run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# creating python shell
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Quote = Quote, User=User, Post=Post,Comment=Comment, Subscribers=Subscribers)


if __name__ == '__main__':
    manager.run()