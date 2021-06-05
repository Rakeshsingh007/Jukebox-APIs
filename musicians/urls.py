
from django.urls import include, path 
from rest_framework import routers
from . import views

app_name = "musicians"

router = routers.DefaultRouter()
router.register('', views.MusiciansView,  basename='musicians')

urlpatterns = [
    path('', include(router.urls)),
    path('list-album-musician/<uuid:id>/', views.ListAlbumMusicians.as_view()),
    path('list-sorted-album/<uuid:id>/', views.ListSortedAlbums.as_view()),
]
