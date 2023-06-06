This is a the Django Rest Framework Quickstart tutorial with BugSnag installed.

Tutorial;
https://www.django-rest-framework.org/tutorial/quickstart/

Follow the steps in the Tutorial to setup a Python ENV and start the server;
```python manage.py runserver```

Navigate to the main page and login with the default admin account;
http://127.0.0.1:8000/

```
user = admin
pass = password123
```

Navigate to the User Groups page;
http://127.0.0.1:8000/groups/?format=api

To send an error, click the 'Extra Actions' dropdown and select 'Notify BugSnag'.