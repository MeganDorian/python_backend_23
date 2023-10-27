from __future__ import absolute_import
from celery import Celery

app = Celery(
    "homework",
    broker="amqp://megan:megan123@localhost/megan_vhost",
    backend="rpc://",
    include=["homework.tasks"],
)
