from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Recipe, Ingredient, Note


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    order = serializers.IntegerField(required=False) 

    class Meta:
        model = Ingredient
        fields = [
            'id', 'name', 'measurement', 'quantity', 'order'
        ]


class NoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    created = serializers.DateTimeField(required=False)

    class Meta:
        model = Note
        fields = [
            'id', 'content', 'created'
        ]


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'author_id', 'name', 'instructions', 'prep_time', 'cook_time',
            'yield_total', 'tags', 'created', 'ingredients', 'notes'
        ]

    def create(self, validated_data):
        '''
        Create the Recipe model and its associated Ingredient(s) and Note(s).
        '''
        # Expects 'author' to be passed in, i.e.: RecipeSerializer.save(author=request.user)
        ingredients_set = validated_data.pop('ingredients', [])
        notes_set = validated_data.pop('notes', [])
        author_id = validated_data.pop('author', None) or validated_data.pop('author_id', None)
        if not isinstance(author_id, int):
            author_id = author_id.id
        model_id = validated_data.pop('id', None)

        recipe = None
        try:
            # Create recipe model
            recipe = Recipe.objects.create(
                author=User.objects.get(id=author_id),
                **validated_data
            )
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist')
        finally:
            # Create ingredients (if any)
            for ingredient_data in ingredients_set:
                ingredient_data.pop('id', None)
                ingredient = Ingredient.objects.create(recipe=recipe, **ingredient_data)

            # Create notes (if any)
            for note_data in notes_set:
                note_data.pop('id', None)
                note = Note.objects.create(recipe=recipe, **note_data)
            
            return recipe

    def update(self, instance, validated_data):
        '''
        Update an existing Recipe model and its associated Ingredient(s) and Note(s).
        '''
        ingredients_set = validated_data.pop('ingredients', [])
        notes_set = validated_data.pop('notes', [])
        author = validated_data.pop('author', None)
        author_id = author or validated_data.pop('author_id', None)
        if not isinstance(author_id, int):
            author_id = author_id.id
        model_id = validated_data.pop('id', None)

        if author != instance.author:
            raise serializers.ValidationError('User is not the author of this recipe')

        # Update recipe model
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update associated ingredients
        for ingredient_data in ingredients_set:
            pk = ingredient_data.pop('id', None)
            ingredient = None
            try:
                ingredient = Ingredient.objects.get(id=pk)
            except Ingredient.DoesNotExist:
                raise serializers.ValidationError('An ingredient does not exist with the given id')
            finally:
                if not ingredient or ingredient.recipe != instance:
                    raise serializers.ValidationError(
                        'The given ingredient was not found nor is associated with this recipe')
                
                for attr, value in ingredient_data.items():
                    setattr(ingredient, attr, value)
                ingredient.save()

        # Update associated notes
        for note_data in notes_set:
            pk = note_data.pop('id', None)
            note = None
            try:
                note = Note.objects.get(id=pk)
            except Note.DoesNotExist:
                raise serializers.ValidationError('A note does not exist with the given id')
            finally:
                if not note or note.recipe != instance:
                    raise serializers.ValidationError(
                        'The given note was not found nor is associated with this recipe')
                    
                for attr, value in note_data.items():
                    setattr(note, attr, value)
                note.save()

        return instance
