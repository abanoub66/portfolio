from django.urls import path
from . import views

urlpatterns = [
    path('', views.number_list_create, name='number_list_create'),
    path('number_list_create', views.number_list_create, name='number_list_create'),
    path('previous_demos', views.previous_demos, name='previous_demos'),
    path('sorting_list/<current>', views.sorting_list, name='sorting_list'),
    path('sorting_list/<current>/sort/<s>', views.sort, name='sort'),
]
