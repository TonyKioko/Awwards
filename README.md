PyAwards
===================
## Description
[PyAwards](https://pyawwards.herokuapp.com/) is a web application where users can post project(s) they have created and get it reviewed by their peers.

------------------------------------------------------------------------

## User Requirements

1. Sign in to the application to start using.
2. Post a project to be rated/reviewed.
3. Rate/ review other users' projects.
4. Search for projects.
5. View projects overall score
6. View my profile page.

### Live Link ###
[PyAwards](https://pyawwards.herokuapp.com/)
## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3.6

### Cloning the repository
```bash
git clone https://github.com/TonyKioko/Awwards && cd Awwards
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.

### Deploying to heroku
Refer to this guide: [deployment to heroku](https://github.com/Benard18/Deployment_to_heroku_django)

## Running the tests
```bash
python manage.py app test
```

## Live Demo

The web app can be accessed from the following link:
[PyAwards](https://pyawards.herokuapp.com/)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Test Driven Development
* Testing was done using python inbuild test tool called unittest


## Known Bugs
There are no known bugs.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license,Copyright (c) 2018 [Tony Kioko](https://github.com/tonykioko/)
