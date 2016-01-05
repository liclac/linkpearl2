from django.core.urlresolvers import reverse
from rest_framework import serializers
from linkpearl_lodestone.models import Race, Server, GrandCompany, Job, Title, Minion, Mount, FreeCompany, Level, Character

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'name', 'slug', 'num_characters')
    
    num_characters = serializers.ReadOnlyField()

class GrandCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandCompany
        fields = ('id', 'name', 'short', 'slug', 'ranks', 'num_characters', 'characters')
    
    ranks = serializers.SerializerMethodField()
    
    num_characters = serializers.ReadOnlyField()
    characters = serializers.HyperlinkedIdentityField(view_name='grandcompany-characters')
    
    def get_ranks(self, obj):
        return [{
            'id': (obj.id * 100) + i,
            'rank': i,
            'name': rank.format(obj.short),
        } for i, rank in enumerate(obj.RANKS)]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name', 'code')

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'name')

class MinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minion
        fields = ('id', 'name')

class MountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mount
        fields = ('id', 'name')

class FreeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeCompany
        fields = ('id', 'lodestone_id', 'name')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'level', 'exp_at', 'exp_of', 'job')

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
