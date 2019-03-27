from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.list_jobs, name='list_jobs')
]
