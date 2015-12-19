from rest_framework import serializers
from linkpearl_lodestone.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
