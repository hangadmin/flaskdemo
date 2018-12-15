from time import sleep

from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/3')


@celery.task
def add(x, y):
    sleep(10)
    return x+y

if __name__ == '__main__':
    # 启动celery celery -A tasks worker --loglevel=info
    # celery -A tasks worker --pool=solo -l info Celery4.1+ 之后新启动命令

    result = add.delay(20, 15)
    print('程序执行结束')
    print(result.backend)