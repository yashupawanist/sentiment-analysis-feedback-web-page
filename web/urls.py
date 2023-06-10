from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('features', views.features, name="features"),
    path('contact', views.contact, name="contact"),
    #path('home', views.home, name='home'),
]