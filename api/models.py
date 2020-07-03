from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from datetime import datetime

from api.validators import valid_quantity, valid_tags
from api.utils import pluralized_measurement
from api.globals import MEASUREMENTS


class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    instructions = models.TextField(max_length=2000)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    yield_total = models.IntegerField()
    tags = models.TextField(validators=[valid_tags])
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    @property
    def number_of_ingredients(self):
        return self.ingredients.count()


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    measurement = models.CharField(max_length=30, choices=MEASUREMENTS)
    quantity = models.IntegerField(validators=[valid_quantity])
    order = models.IntegerField()

    def __str__(self):
        measurement = pluralized_measurement(self.measurement, self.quantity)
        return f'{self.recipe.name} - {self.quantity} {measurement} of {self.name}'

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.recipe.number_of_ingredients
        super(Ingredient, self).save(*args, **kwargs)


class Note(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.recipe.name} - {self.content}'
