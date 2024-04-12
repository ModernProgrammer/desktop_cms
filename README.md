# Django Wagtail Setup
Need to run the virtual environment which contains all of the required packages.

**Activate Environment**

```source ./venv/bin/activate```

**Deactivate Environment**

```deactivate```

Once you are in the the virtual env, run the following command

```pip install -r requirements.txt```

_Note: No need to run migrations since we are currently only using the Sql Lite Database, might change to PostgreSQL_

Run the following, inside the headless_cms folder, to start the server

```python manage.py runserver```
