from django.shortcuts import render

# Create your views here.
# myapp/modls.py

from django.shortcuts import  render
from django.views import View
from django.http import HttpResponse
from models import Food


class FoodLostView(View):
    tamplate_name = 'food_list.html'

    def get(self, request):
        foods = Food.objects.all()
        return render(request, self.tamplate_name, {'foods': foods})