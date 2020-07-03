# Recipe sharing project
> Intends to be Django Rest Framework microservice API

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