#!/bin/bash
python manage.py makemigrations student
python manage.py migrate
