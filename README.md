# MavLost

Web application to quickly and easily report and find lost items around campus.



## Local Dev Setup for group

### 1. create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 2. install dependencies

```
python -m pip install "Django==5.2.19" Pillow
```

### 3. create local database (each member must create own local database bc database not shared thru github)

```
python manage.py migrate
```

### 4. create local test account (each member needs own local account to login and test)

#### 4.1.
```
python manage.py shell
```

#### 4.2.
```
from django.contrib.auth import get_user_model
from getpass import getpass

User = get_user_model()
User.objects.create_user(
    username='mavlost_test',
    password=getpass('Choose a test password: '),
)
```

#### 4.3. enter password when prompted

#### 4.4. exit shell
```
exit()
```

### 5. start development server

#### 5.1.
```
python manage.py runserver
```

#### 5.2.
Open http://127.0.0.1:8000/ in browser

(Control + C in terminal to stop server)
