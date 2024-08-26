"""
URL mapping for the recipe app is defined in app/recipe/urls.py. The URL mapping is then imported into the main project urls.py file.
"""

from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
] 