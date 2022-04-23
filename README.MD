

![Docker Automated build](https://img.shields.io/docker/automated/k1wsatz/camp-app-one) 
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/k1wsatz/camp-app-one)


![Logo](https://cdn4.iconfinder.com/data/icons/transportation-190/1000/camper_camper_car_camp_car_campsite_camper_van_bus-512.png)


# Camp app

This is a simple camp app for people to search, add and reserve camping.

## Demo:
http://mwcamp.herokuapp.com/
## Features


- Fullscreen mode
- Cross platform


## Installation

Clone camp-app-one with git

```bash
  git clone git@github.com:k1wsatz/camp-app-one.git
  cd camp-app-one
  python manage.py runserver
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. You can also use file `.env-default`, put there your own data and rename it to `.env` than run command `source env/.env` in terminal to activate.

`POSTGRES_USER=`

`POSTGRES_PASSWORD=`

`POSTGRES_DB=`

`DATABASE_URL=`

`DEBUG=`

`SECRET_KEY=`

`DJANGO_ALLOWED_HOSTS=`

`DJANGO_SU_NAME=`

`DJANGO_SU_EMAIL=`

`DJANGO_SU_PASSWORD=`

`DJ_GROUP_REGULAR='regular'`

`DJ_GROUP_OWNERS='owners'`
## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Authors

- [@k1wsatz](https://www.github.com/k1wsatz

