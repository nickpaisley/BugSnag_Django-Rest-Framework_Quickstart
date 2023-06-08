This is the Django Rest Framework Quickstart tutorial with BugSnag installed.

Tutorial:
https://www.django-rest-framework.org/tutorial/quickstart/

Follow the steps in the Tutorial to setup a Python ENV and start the server:
```python manage.py runserver```

Navigate to the main page and login with the default admin account:
```http://127.0.0.1:8000/```

```Username = admin```

```Password = password123```


Navigate to the User Groups page:
```http://127.0.0.1:8000/groups/?format=api```

To send an error, click the 'Extra Actions' dropdown and select 'Notify BugSnag'.

The function that calls this notifier is found on line 39 in:
```/tutorial/tutorial/quickstart/views.py```

## Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```