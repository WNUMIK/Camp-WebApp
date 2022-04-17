from django.urls import path

from . import views

app_name = 'campings'

urlpatterns = [
    path('create', views.CreateCampingView.as_view(), name='create-camping'),
    path('reserve', views.ReserveCampingView.as_view(), name='reserve-camping'),
    path('list', views.CampingListView.as_view(), name='list-camping'),
    path('search', views.SearchResultsListView.as_view(), name='search-camping'),
    path('details/<slug:slug>', views.CampingDetailView.as_view(), name='detail-camping'),
]