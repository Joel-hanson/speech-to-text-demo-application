#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
make migrate

# Start frontend
echo "Starting frontend"
make run-frontend &

# Start backend
echo "Starting backend"
make run &

# Start celery
echo "Starting celery"
make run-celery &

# export CELERY_BROKER_URL="amqp://${RABBITMQ_DEFAULT_USER:-guest}:${RABBITMQ_DEFAULT_PASS:-guest}@${RABBITMQ_HOST:-rabbitmq}:${RABBITMQ_PORT:-5672}/"

# echo "get celery registred tasks"
# make celery-get-registered-tasks &

# echo "debug celery"
# make celery-debug &>/dev/null &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
