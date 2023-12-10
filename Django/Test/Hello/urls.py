

from django.urls import path
from .views import FoodLostView

urlpatterns = [
    path('food/', FoodLostView.as_view(), name='food_list'),
]