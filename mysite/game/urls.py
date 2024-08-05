from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("new/", views.buildDeck, name = "newGame"),
    path("home/",views.HomeView.as_view(), name='home-template'),
]