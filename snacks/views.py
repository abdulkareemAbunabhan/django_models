from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Snack

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SnacksPageView(ListView):
    template_name= 'snacks.html'
    model = Snack
    context_object_name = "Snacks"