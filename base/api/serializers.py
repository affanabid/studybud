# Python objects cannot be passed through response method of rest framework so we need serializers
# Serializers include classes take python object and convert to json or js objects

from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'