from django.urls import path

from . import views

app_name = 'campings'

urlpatterns = [
    path('create', views.CreateCampingView.as_view(), name='create-camping'),
]