# Developer Log

##### Virtual Environment/Getting Started With Django

    1. cd into pizzaria folder
    2. `pip install --user virtualenv`
    3. `virtualenv 11_env`
    4. Activate the virtual environment with `source 11_env/bin/activate`

##### Installing Django

    1. While the virtual environment is active (11_env), install Django with
        `pip install Django`

##### Creating a Project in Django

    1. In the activated virtual environment (11_env), type the following command:
    `django-admin.py startproject pizzeria .` Don't forget to add
    the `.` at the end of the command! 
    2. Create the database with `python manage.py migrate`.  
    * You will see a db.sqlite3 file in yoru root project folder. 
    3. Check if Django set up the server properly with the following
    command `python manage.py runserver`. Open up a browser and 
    type `localhost:8000` for the URL.

##### Starting an APP
    1. Make sure the virtual environment is still activated. If not, 
    use `source 11_env/bin/activate` and you will see an `11_env` next
    to the terminal folder.
    2. `python manage.py startapp pizzas`. 

##### Defining Models
    1. Open models.py and check out the code posted there.
    2. Open settings.py and check under `INSTALLED_APPS` tuple insert `pizzas`,
    3. In terminal, type the following command:
    `python manage.py makemigrations pizzas`
    4. In terminal, type the following command:
    `python manage.py migrate`

##### Creating a Superuser
    1. `python manage.py createsuperuser`
    2. Create a Username and Password.
    3. Open admin.py file and write out the admin register and import code.
    4. Open a web browser and head to `http://localhost:8000/admin/`
    5. Login.

##### Defining the Entry Model
    1. `class Entry(models.Model):`
    2. `python manage.py makemigrations pizzas