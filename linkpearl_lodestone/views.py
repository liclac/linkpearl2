from rest_framework import viewsets
from linkpearl_lodestone.serializers import ServerSerializer, CharacterSerializer
from linkpearl_lodestone.models import Server, Character

class ServerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServerSerializer
    queryset = Server.objects.all()

class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.select_related('user').prefetch_related('jobs', 'minions', 'mounts').all()
