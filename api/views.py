from django.http import Http404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.models import Recipe, Ingredient, Note
from api.serializers import RecipeSerializer

from functools import reduce
from operator import or_


class RecipeListView(ListAPIView):
    '''
    Class-based (List) view for Recipe(s).
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializer
    model = Recipe
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.prefetch_related('ingredients', 'notes')


class RecipeSearchView(ListAPIView):
    '''
    Provides an interface to search all recipe models and return paginated results.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializer
    model = Recipe
    paginate_by = 20

    def get_queryset(self):
        '''
        Perform search query by parsing #hashtags and searching by tag
        and also by searching through recipes who are associated with
        ingredients that match a given word (that does not contain a #)
        on the suppliedd query.
        '''
        query = self.request.GET['query']
        words = query.split(' ')

        # separate hashtags from ingredient names
        tags = []
        ingredients = []
        for word in words:
            if '#' in word:
                word = word.replace('#', '')
                tags.append(word)
            else:
                ingredients.append(word)
        
        # find recipes with the given hashtags and/or with ingredient names
        queryset = self.model.objects\
                .prefetch_related('ingredients', 'notes')\
                .filter(
                    reduce(or_, [Q(tags__contains=tag) for tag in tags])\
                    | reduce(or_, [Q(ingredients__name__contains=name) for name in ingredients])
                )
        
        return queryset


class RecipeView(APIView):
    '''
    Retrieve, Update or Delete a Recipe.
    '''
    permission_classes = [IsAuthenticated]

    def get_model(self, pk):
        try:
            return Recipe.objects.prefetch_related('ingredients', 'notes').get(id=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_model(pk)
        recipe_dict = RecipeSerializer(recipe).data
        return Response(recipe_dict)

    def post(self, request, pk, format=None):
        serialized = RecipeSerializer(data=request.data)
        if serialized.is_valid():
            response = RecipeSerializer(serialized.save(author=request.user)).data
        else:
            response = serialized.errors
        return Response(response)

    def put(self, request, pk, format=None):
        recipe = self.get_model(pk)
        serialized = RecipeSerializer(recipe, data=request.data, partial=True)
        if serialized.is_valid():
            response = RecipeSerializer(serialized.save(author=request.user)).data
        else:
            response = serialized.errors
        return Response(response)

    def delete(self, request, pk, format=None):
        # To be supported in the future?
        pass
