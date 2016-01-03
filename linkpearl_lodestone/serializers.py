from rest_framework import serializers
from linkpearl_lodestone.models import Race, Server, GrandCompany, Job, Title, Minion, Mount, FreeCompany, Character

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
    
    population = serializers.SerializerMethodField()
    
    def get_population(self, obj):
        return obj.characters__count

class GrandCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandCompany

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title

class MinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minion

class MountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mount

class FreeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeCompany

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
