# Meetup
Meetup app built with Django

## Setup steps
  1. Create a remote repository in GitHub named Meetup
  2. Create a directory called Meetup in your local machine
  3. Initialize git and change the branch name from masters to main
  4. Ensure python (v3.x.x) is installed
  5. Ensure the python and pylance extensions are installed
  6. Ensure to set the default language server is set to python -> *navigate to Preferences: Open Settings (JSON) and set it to: {"python.  languageServer": "Pylance", "python.analysis.typeCheckingMode": "strict"}*
  7. Ensure to set the python interpreter to pylance at the bottom-right status bar of visual studio
  8. Create a .gitignore file and add a the extensions you want to skip. You may add README file to document steps of reproducing the project 


## Django 
  1. Create a django admin project folder -> *django-admin startproject django_meetup*
  2. Create a django app folder inside project folder -> *python3 manage.py startapp meetup*
  3. Create a virtual environment -> *python3 -m venv django_meetup* and run *python3 -m pip freeze > requirements.txt*