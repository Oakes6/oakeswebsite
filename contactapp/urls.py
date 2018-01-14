from django.conf.urls import url, include
from . import views

app_name = 'contactapp'

urlpatterns = [
    url(r'^contact/$',views.email,name="contact"),
    url(r'^thanks/$',views.thanks,name="thanks"),
]
