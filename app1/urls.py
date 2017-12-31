from django.conf.urls import url, include
from . import views

app_name = 'app1'

urlpatterns = [
    url(r'^workexperience', views.WorkExperienceView.as_view(),name="workexperience"),
]
