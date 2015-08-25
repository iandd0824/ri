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
