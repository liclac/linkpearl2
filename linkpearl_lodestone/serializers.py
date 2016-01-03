from rest_framework import serializers
from linkpearl_lodestone.models import Server, Character

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
    
    population = serializers.SerializerMethodField()
    
    def get_population(self, obj):
        return obj.characters.count()

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
