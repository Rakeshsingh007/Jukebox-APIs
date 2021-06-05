from rest_framework import serializers
from . models import MusicAlbums
from musicians.serializers import MusiciansSerializer



class AlbumSerializer(serializers.ModelSerializer):
  album_genre_related = serializers.CharField(source='get_album_genre_display', read_only= True)
  album_musicians = MusiciansSerializer(read_only=True, many=True)

  class Meta:
      model = MusicAlbums
      fields = ["id", "album_token", "album_name", "album_release_date", "album_genre_related", "album_genre", "album_price", "album_description", "album_musicians"]

      extra_kwargs = {
            "album_genre": {"write_only": True}
        }

      read_only_fields = ["album_token",]

