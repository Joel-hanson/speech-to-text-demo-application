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

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
