# ri	

## Server 

#### [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Install virtualenv via pip:

```sh
$ pip install virtualenv
```
Basic usage

1. Create a virtual environment for a project

```sh
$ cd server
$ virtualenv venv
```

2. To begin using the virtual environment, it needs to be activated:
```sh
$ source venv/bin/activate
```

3. Install packages as usual, for example:
```sh
$ pip install requests
```

4. Install requirement.txt
```sh
$ pip install -r requirements.txt
```

5. If you are done working in the virtual environment for the moment, you can deactivate it:

```sh
$ deactivate
```

#### Run server

1. Move to folder ptsd

```sh
$ cd ptsd
```

2. Run server

```sh
$ python manage.py runserver
```

### Create new user

With Python shell

```sh
$ python manage.py shell
```

```sh
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
>>> from mongoengine.django.auth import User
>>> User.create_user('username','password','email')
<User: username>
```

```sh
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
>>> from mongoengine.django.auth import User
>>> user = User()
>>> user.username = 'user3'
>>> user.password = 'pass'
>>> user.email = 'user3@gmail.com'
>>> user.name = 'testname'
>>> user.save()
```
