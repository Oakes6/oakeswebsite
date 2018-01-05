from django.conf.urls import url, include
from . import views

app_name = 'app1'

urlpatterns = [
    url(r'^workexperience/', views.WorkExperienceView.as_view(),name="workexperience"),
    url(r'^about/',views.AboutView.as_view(),name="about"),
    url(r'^extracurriculars/',views.ExtracurricularsView.as_view(),name="extracurriculars"),
    url(r'^skills/',views.Skills.as_view(),name="skills"),
]
