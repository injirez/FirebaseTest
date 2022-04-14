from django.urls import path
from . import views

urlpatterns = [
    path('get_countries/', views.get_countries),
    path('add_country/', views.add_country, name='add_country'),
    path('post_country/', views.post_country),
]