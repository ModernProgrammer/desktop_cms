# Django Wagtail Setup

Need to run the virtual environment which contains all of the required packages.

**Activate Environment**

```source ./venv/bin/activate```

**Deactivate Environment**

```deactivate```

Once you are in the the virtual env, navigate to the inside the headless_cms folder.

Once in that directory, run the following command to install dependencies

```pip install -r requirements.txt```
```python3 -m pip install django-cors-headers```

Note: No need to run migrations since we are currently only using the Sql Lite Database, might change to PostgreSQL_

Run the following to start the server

For local:
```python3 manage.py runserver```

For Server:
```python3 manage.py runserver <server IP>:<port>```
