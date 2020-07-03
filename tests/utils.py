from django.contrib.auth.models import User

from api.models import Recipe, Ingredient, Note

import random
import string


BASE_URL = 'http://127.0.0.1:8000'


def random_string(depth=10):
    return ''.join([random.choice(string.ascii_letters) for x in range(depth)])


def build_user():
    '''
    Build a new user and return a dict containing the raw username, password and the user model.
    '''
    username, email, password = [
        random_string(), random_string(), random_string()
    ]
    user = User.objects.create_user(username, email, password)
    return {
        'username': username,
        'password': password,
        'user': user
    }


def fake_data(user, depth=100):
    '''
    Create a recipe and an associated Ingredient and Note.
    '''
    for x in range(depth):
        r = Recipe(
            author=user,
            name=f'test-{random_string()}',
            instructions='\n'.join(['1. Do this', '2. Then do this next']),
            prep_time=30 + x,
            cook_time=30,
            yield_total=1,
            tags='tag1,tag2'
        )
        r.save()
        i = Ingredient(recipe=r, name='Beans', measurement='cup', quantity=random.randint(1, 12))
        i.save()
        n = Note(recipe=r, content=random_string(100))
        n.save()
