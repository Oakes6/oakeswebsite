from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from contactapp.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

# home page view
class HomeView(TemplateView):
    template_name = 'home.html'

# work experience
class WorkExperienceView(TemplateView):
    template_name = 'workexperience.html'

# about
class AboutView(TemplateView):
    template_name = "about.html"

# extracurriculars
class ExtracurricularsView(TemplateView):
    template_name = "extracurriculars.html"

# Skills
class Skills(TemplateView):
    template_name = "skills.html"

# Contact Form View
# class ContactView(FormView):
#     template_name = "contactapp/contactpage.html"
#     form_class = ContactForm
#     success_url = '/thankyou/'
#
#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)

def email(request):

    if request.method == "GET":
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['tanner.w.oakes@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Thank you for your message!')
            # return redirect('thanks')
    return render(request, "contactapp/contactpage.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message!')
