from typing import Any
from django.db import models
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
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

class SnackDetailPageView(DetailView):
    template_name = 'snack_detail.html'
    models = Snack
    def get_queryset(self):
        return Snack.objects.all()