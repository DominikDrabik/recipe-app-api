"""
Serialiers for recipe APIs 
"""

from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""

    # Here it tells django we want to use the model Recipe and the fields we want to use
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'link')
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail objects"""
    # Here we are extending the RecipeSerializer and adding the extra fields
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ('ingredients', 'tags')
        read_only_fields = ('id',)
