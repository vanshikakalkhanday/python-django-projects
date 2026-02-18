# Combined Django Projects

This repository contains three Django projects:

1. Inventory Project

   Branch: feature/inventory_project

2. Blog Project

   Branch: feature/newblog

3. Admin Customization Project

   Branch: feature/adminproject

-------------------------------------

## Requirements

- Python 3.10+

- Django (see requirements.txt)

-------------------------------------

## Setup Instructions

1. Clone repository

2. Create virtual environment:

   python -m venv venv

3. Activate environment:

   venv\Scripts\activate   (Windows)

   source venv/bin/activate (Mac/Linux)

4. Install dependencies:

   pip install -r requirements.txt

-------------------------------------

## Running a Project

Example for Inventory Project:

cd inventory_project

python manage.py migrate

python manage.py runserver

Same steps apply for other projects.
 