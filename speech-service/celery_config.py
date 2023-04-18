import urllib.request

from celery import Celery
from celery.utils.log import get_task_logger
from decouple import config
from kombu import Exchange, Queue

# Initialize celery
# # redis broker
# REDIS_URL = "redis://{host}:{port}/{db}".format(
#     host=config("REDIS_HOST", "redis", cast=str),
#     port=config("REDIS_PORT", "6379", cast=int),
#     db=config("REDIS_DB", default=1, cast=int),
# )
# Rabbitmq broker
RABBITMQ_URL = "amqp://{user}:{password}@{host}:{port}/".format(
    user=config("RABBITMQ_USER", "guest", cast=str),
    password=config("RABBITMQ_PASSWORD", "guest", cast=str),
    host=config("RABBITMQ_HOST", "rabbitmq", cast=str),
    port=config("RABBITMQ_PORT", "5672", cast=int),
    # vhost=config("RABBITMQ_VHOST", "rabbitmq", cast=str),
)


# postgres backend db
DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{db}".format(
    user=config("DB_USER", "postgres", cast=str),
    password=config("DB_PASSWORD", "postgres", cast=str),
    host=config("DB_HOST", "db", cast=str),
    port=config("DB_PORT", "5432", cast=int),
    db=config("DB_NAME", "postgres", cast=str),
)
BACKEND_URL = "db+" + DATABASE_URL

# # dead letter queue
# dead_letter_queue_option = {
#     "x-dead-letter-exchange": "dlx",
#     "x-dead-letter-routing-key": "dead_letter",
# }
# default_exchange = Exchange("default", type="direct")
# dlx_exchange = Exchange("dlx", type="direct")
# default_queue = Queue(
#     "default",
#     default_exchange,
#     routing_key="default",
#     queue_arguments=dead_letter_queue_option,
# )
# dead_letter_queue = Queue("dead_letter", dlx_exchange, routing_key="dead_letter")

# celery config
celery = Celery("tasks", broker=RABBITMQ_URL, backend=BACKEND_URL)

# celery.conf.task_queues = (default_queue, dead_letter_queue)
# celery.conf.task_default_queue = "default"
# celery.conf.task_default_exchange = "default"  # type: ignore
# celery.conf.task_default_routing_key = "default"  # type: ignore
