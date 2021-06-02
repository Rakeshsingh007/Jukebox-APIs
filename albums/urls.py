from django.urls import path
from . import views

app_name = 'webscraper'

urlpatterns = [
    path('/', views.CovidCaseWebScraper.as_view()),
]