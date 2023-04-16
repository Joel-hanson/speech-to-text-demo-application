#!/bin/bash

# Start backend
# echo "Starting backend"
# make run &

# start celery
echo "Starting celery"
make run-celery &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
