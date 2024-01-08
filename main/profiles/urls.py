from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles_list, name='profiles_list'),
    path('add_resident/', views.add_resident, name='add_resident'),
    path('add_staff/', views.add_staff, name='add_staff'),
    # add other URLs here
]