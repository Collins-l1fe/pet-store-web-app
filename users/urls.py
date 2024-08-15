from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('hi/', views.hellohtml, name='hellohtml'),
]
