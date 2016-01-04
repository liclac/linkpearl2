from rest_framework import serializers
from linkpearl_lodestone.models import Race, Server, GrandCompany, Job, Title, Minion, Mount, FreeCompany, Level, Character

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['id', 'name', 'slug', 'population']
    
    population = serializers.ReadOnlyField()

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

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id', 'lodestone_id', 'user',
            'server', 'first_name', 'last_name', 'title',
            'race', 'clan', 'gender',
            'gc', 'gc_rank', 'fc',
            'levels', 'minions', 'mounts',
        )
    
    levels = LevelSerializer(many=True, read_only=True)
