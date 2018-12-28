from flask_migrate import MigrateCommand
from flask_script import Manager

from flaskdemo import create_app

app = create_app('develop')
manage = Manager(app=app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()