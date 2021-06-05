from rest_framework import serializers
from . models import Musicians



class MusiciansSerializer(serializers.ModelSerializer):
  musicians_type_related = serializers.CharField(source='get_musicians_type_display', read_only=True)

  class Meta:
    
      model = Musicians
      fields = ["id", "musicians_token", "musicians_name", "musicians_type_related", "musicians_type"]

      extra_kwargs = {
            "musicians_type": {"write_only": True}  
        }

      read_only_fields = ["musicians_token",]