from celery import Celery
from celery.utils.log import get_task_logger
from decouple import config

RABBITMQ_URL = "amqp://{user}:{password}@{host}:{port}/".format(
    user=config("RABBITMQ_USER", "guest", cast=str),
    password=config("RABBITMQ_PASSWORD", "guest", cast=str),
    host=config("RABBITMQ_HOST", "rabbitmq", cast=str),
    port=config("RABBITMQ_PORT", "5672", cast=int),
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

# celery config
celery = Celery("tasks", broker=RABBITMQ_URL, backend=BACKEND_URL)
