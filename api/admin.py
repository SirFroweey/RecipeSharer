from django.contrib import admin
from api.models import Recipe, Ingredient, Note


class RecipeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Recipe, RecipeAdmin)


class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingredient, IngredientAdmin)


class NoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Note, NoteAdmin)
