from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# home page view
class HomeView(TemplateView):
    template_name = 'home.html'

# work experience
class WorkExperienceView(TemplateView):
    template_name = 'app1/workexperience.html'
