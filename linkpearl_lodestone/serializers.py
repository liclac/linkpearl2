from rest_framework import serializers
from linkpearl_lodestone.models import Server, Character

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
