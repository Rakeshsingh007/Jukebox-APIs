from django.urls import include, path 
from rest_framework import routers
from . import views

app_name = "albums"

router = routers.DefaultRouter()
router.register('', views.MusicAlbumsView,  basename='albums')

urlpatterns = [
    path('', include(router.urls)),
]
