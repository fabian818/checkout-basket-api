# Checkout Basket API

A project to manage checkout basket promos

## Getting Started

### Prerequisites

```
Python 3.6
Pyenv (or some python environment manager)
PostgreSQL 13.2
```

Or just install Docker and run the app with docker-compose

### Installing

Install dependences

```
pip install -r source/requirements.txt
```

Create a database with postgresql

```
create database checkout_basket_dev;
```

Put the .env file at the root of the project, you can guide from [test.env](https://github.com/fabian818/checkout-basket-api/blob/main/test.env)

Alternatively you can just run:

```
docker-compose up -d
```

### Usage

Run the server with

```
./source/manage.py runserver
```

Read the documentation at GET /redoc and start to use the API 🥳

## Running the tests

To run automated tests:

```
./source/manage.py test apps.api.tests
```

To run code quality (Pylint) run:

```
pylint --load-plugins=pylint_django --django-settings-module=checkout_basket_api.settings --exit-zero source/.
```

Alternatively you can just run:

```
docker-compose -f docker-compose.test.yml up --exit-code-from api --build
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Docker](https://www.docker.com/) - Container Engine

## Authors

* **Fabian Peña** - *Initial work* - [fabian818](https://github.com/fabian818)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.