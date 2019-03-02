from flask_migrate import MigrateCommand
from flask_script import Manager

from celery_runner import make_celery
from flaskdemo import create_app

# def make_celery(app):
#     celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
#     TaskBase = celery.Task
#     class ContextTask(TaskBase):
#         abstract = True
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#     celery.Task = ContextTask
#     return celery

app = create_app('develop')
manage = Manager(app=app)
celery = make_celery(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()