from django.urls import path, include
from . import views


urlpatterns = [
    path('recipe/list', views.RecipeListView.as_view()),
    path('recipe/search', views.RecipeSearchView.as_view()),
    path('recipe', views.RecipeView.as_view(), {'pk': None}),
    path('recipe/<int:pk>', views.RecipeView.as_view())
]
