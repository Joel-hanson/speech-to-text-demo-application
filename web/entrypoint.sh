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

echo "Starting kafka connectors"

echo "Starting s2t-upload-event-source-connector"
make start-s2t-upload-event-source-connector &

echo "Starting s2t-http-sink-connector"
make start-s2t-http-sink-connector &

# wait for the connectors to start
sleep 10

# Get the list of connectors
CONNECTORS=$(curl -H "Accept:application/json" connect:8083/connectors)
echo "Connectors: $CONNECTORS"

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
