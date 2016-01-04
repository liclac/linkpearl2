from django.db.models import Count
from rest_framework import viewsets
from linkpearl.pagination import UnlimitedPageNumberPagination
from linkpearl_lodestone.serializers import RaceSerializer, ServerSerializer, GrandCompanySerializer, JobSerializer, TitleSerializer, MinionSerializer, MountSerializer, FreeCompanySerializer, CharacterSerializer
from linkpearl_lodestone.models import Race, Server, GrandCompany, Job, Title, Minion, Mount, FreeCompany, Character

class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RaceSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Race.objects.all()

class ServerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServerSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Server.objects.annotate(population=Count('characters')).all()

class GrandCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GrandCompanySerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = GrandCompany.objects.annotate(members=Count('characters')).all()

class JobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Job.objects.all()

class TitleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()

class MinionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MinionSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Minion.objects.all()

class MountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MountSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Mount.objects.all()

class FreeCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FreeCompanySerializer
    queryset = FreeCompany.objects.all()

class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.select_related('user').prefetch_related('levels', 'minions', 'mounts').all()
