#!/bin/sh

echo "Running database migrations..."

flask db upgrade

echo "Starting Gunicorn..."

gunicorn --bind 0.0.0.0:$PORT run:app