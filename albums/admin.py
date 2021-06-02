from django.contrib import admin
from django.contrib.auth.models import User, Group
from . models import MusicAlbums



class MusicAlbumsAdmin(admin.ModelAdmin):
	ordering = ('id',)
	list_per_page = 50
	list_display =  ('album_name','album_release_date','album_genre','album_price', 'album_description')
	search_fields = ('album_name',)

admin.site.register(MusicAlbums,MusicAlbumsAdmin)