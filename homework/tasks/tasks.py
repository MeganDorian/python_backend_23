from __future__ import absolute_import

import string

from homework.tasks.celery import app
import time
import random


@app.task
def longtime_task_example(x):
    print(f"long time task begins with {x}")
    time.sleep(5)
    id = random.randrange(10, 10000) * x
    print("long time task finished")
    return id
