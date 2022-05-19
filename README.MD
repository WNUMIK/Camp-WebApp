[![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/k1wsatz/charity/issues)
[![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://github.com/k1wsatz/charity/network)
[![](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://github.com/k1wsatz/charity/stargazers)
[![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://github.com/k1wsatz/charity/stargazers)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/k1wsatz/camp-app-one)
[![GitHub issues](https://img.shields.io/github/issues/k1wsatz/camp-app-one)](https://github.com/k1wsatz/camp-app-one/issues)
[![GitHub forks](https://img.shields.io/github/forks/k1wsatz/camp-app-one)](https://github.com/k1wsatz/camp-app-one/network)
[![GitHub stars](https://img.shields.io/github/stars/k1wsatz/camp-app-one)](https://github.com/k1wsatz/camp-app-one/stargazers)

# Camp app
This is a simple camp app for people to search, add and reserve camping.
![Logo](https://cdn4.iconfinder.com/data/icons/transportation-190/1000/camper_camper_car_camp_car_campsite_camper_van_bus-512.png)



# Images:
![Screenshot 2022-04-24 at 11 48 24](https://user-images.githubusercontent.com/98759136/164970647-a8b481ea-ac10-47bc-8f7b-bae597e270b4.png)
----------------------------------------------------------------------------------------------------------------------------------------------------------

![register](https://user-images.githubusercontent.com/98759136/164970754-b620678d-02d9-4efd-ad60-822ed49352a3.png)
----------------------------------------------------------------------------------------------------------------------------------------------------------

![login](https://user-images.githubusercontent.com/98759136/164970766-d77db05e-3fde-4cd7-89dc-ef3a438fa4e4.png)


## Demo:
http://mwcamp.herokuapp.com/




## Features


- Fullscreen mode
- Cross platform
- Login & registry
- Reserve or Add
- Detail List



## Installation


Clone camp-app-one with git:

```bash
  git clone git@github.com:k1wsatz/camp-app-one.git
  cd camp-app-one
```

    
Setup a local development environment:

`pipenv shell`

Install development dependencies:

`pipenv install -r requirements.txt`

Migrate Database:

`python manage.py migrate`

Run the web application locally:

`python manage.py runserver`


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

- [@k1wsatz](https://www.github.com/k1wsatz)

