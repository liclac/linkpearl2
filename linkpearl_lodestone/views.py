from rest_framework import viewsets
from linkpearl_lodestone.serializers import CharacterSerializer
from linkpearl_lodestone.models import Character

class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.prefetch_related('jobs', 'minions', 'mounts').all()
