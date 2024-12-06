#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert statis asset files
python manage.py collectstatic --no-input

# Apply any outstanding migrations
python manage.py migrate