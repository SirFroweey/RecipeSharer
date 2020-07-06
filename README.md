# Recipe sharing project
> Intends to be Django Rest Framework microservice API

## Requirements
- django
- django rest framework
- django-rest-auth
- django-allauth

## Technical spec
https://docs.google.com/document/d/1bkJeIOd7LjtO9bdxMe1jvN96qv_7cpt44X1WgwgKCu8/edit#heading=h.m148he27dc58

## Instructions
1. `pipenv --python 3.8`
2. `pipenv install`
3. `pipenv shell`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python manage.py runserver`


## Endpoints
* /api/recipe/list (GET)
> List all recipes endpoint.

* /api/recipe/ (POST)
> Create a new Recipe endpoint
Example json body:
```
{
    "name": "Example1",
    "instructions": "Blah!",
    "prep_time": 30,
    "cook_time": 50,
    "yield_total": 1,
    "tags": "hello,world",
    "notes": [
        {"content": "Nothing really..."}
    ],
    "ingredients": [
        {"name": "Rice", "measurement": "ounces", "quantity": 1}
    ]
}
```

* /api/recipe/{id} (GET)
> Retrieve an existing recipe

* /api/recipe/{id} (PUT)
> Update an existing recipe
Example json body:
```
{
    "name": "Example1",
    "instructions": "Blah!",
    "prep_time": 30,
    "cook_time": 50,
    "yield_total": 1,
    "tags": "hello,world",
    "notes": [
        {"content": "Nothing really..."}
    ],
    "ingredients": [
        {"name": "Rice", "measurement": "ounces", "quantity": 1}
    ]
}
```

* /api/recipe/search (GET)
> Search for recipes using hashtags or ingredient names, separated by spaces, i.e.: #tag #tag2 beans rice


* /openapi
> OpenAPI graph

* /registration
> Create an account

* /api/auth
> DRF auth endpoints (login, logout)