from django.urls import path
from . import views
app_name = 'formapp'
urlpatterns=[
    path('formapp', views.insert),
]