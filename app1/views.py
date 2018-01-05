from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# home page view
class HomeView(TemplateView):
    template_name = 'home.html'

# work experience
class WorkExperienceView(TemplateView):
    template_name = 'app1/workexperience.html'

# about
class AboutView(TemplateView):
    template_name = "app1/about.html"

# extracurriculars
class ExtracurricularsView(TemplateView):
    template_name = "app1/extracurriculars.html"

# Skills
class Skills(TemplateView):
    template_name = "app1/skills.html"
