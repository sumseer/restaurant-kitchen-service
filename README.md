# Kitchen Restaurant Management Service

A Django-based web application for managing a restaurant kitchen, including managing dishes, dish types, and cooks. This project provides an intuitive interface for kitchen staff to organize, track, and update dish details.

## Features

- **Dish Management**: Add, update, and delete dishes.
- **Dish Types**: Categorize dishes by type for better organization.
- **Cook Management**: Assign cooks to dishes.
- **Search**: Filter dishes and dish types by name.
- **Authentication**: Login and manage access to the application.

## Requirements

- Python 3.12+
- Django 4.2+
- PostgreSQL (or other database systems supported by Django)
- Optional: Install `ruff` for linting and `black` for code formatting

## Installation

   ```bash
   git clone https://github.com/yourusername/kitchen-restaurant-management.git
   cd kitchen-restaurant-management
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver
