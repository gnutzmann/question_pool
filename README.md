# QUESTION POOL

1. CREATE ENVIRONMENT

   Here you can use the name for the directory you prefer. I suggest "django"

   > mkdir django

   > cd django

   > python -m venv env

2. ACTIVATE VIRTUAL ENVIRONMENT

   > source env/bin/activate

3. INSTALL DJANGO

   > pip install django

4. CLONE REPOSITORY

   > git clone https://github.com/gnutzmann/question_pool.git

5. CREATE DATABASE

   > cd question_pool

   > python manage.py migrate

6. CREATE SUPER USER FOR ADMIN PAGE

   > python manage.py createsuperuser

7. RUN SERVER

   > python manage.py runserver

8. ACCESS ADMIN PAGE

   http://127.0.0.1:8000/admin
