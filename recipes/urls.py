from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.recipe_dash, name='dashboard'),
    url('dashboard/', views.recipe_dash, name='dashboard')
]
