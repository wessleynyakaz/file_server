#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Activate the virtual environment
source venv/bin/activate

echo "Resetting the database and migrations..."

# Check if the migrations directory exists before removing it
if [ -d "api/migrations" ]; then
    rm -r api/migrations
    echo "Migrations deleted"
else
    echo "Migrations directory does not exist. Skipping removal."
fi

# Check if the media directory exists before removing it
if [ -d "media" ]; then
    rm -r media
else
    echo "Media directory does not exist. Skipping removal."
fi

# Drop and recreate the database
rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py makemigrations api
python3 manage.py migrate

# Start the server
python3 manage.py runserver