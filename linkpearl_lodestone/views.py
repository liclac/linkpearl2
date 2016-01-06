from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from linkpearl.pagination import UnlimitedPageNumberPagination
from linkpearl_lodestone.serializers import RaceSerializer, ServerSerializer, GrandCompanySerializer, JobSerializer, TitleSerializer, MinionSerializer, MountSerializer, FreeCompanySerializer, CharacterSerializer
from linkpearl_lodestone.models import Race, Server, GrandCompany, Job, Title, Minion, Mount, FreeCompany, Character

class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RaceSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Race.objects.annotate(num_characters=Count('characters')).all()
    
    @list_route()
    def stats(self, request, **kwargs):
        return Response(
            Character.objects.values('race', 'clan', 'gender').annotate(num_characters=Count('clan'))
        )

class ServerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServerSerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = Server.objects.annotate(num_characters=Count('characters')).all()

class GrandCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GrandCompanySerializer
    pagination_class = UnlimitedPageNumberPagination
    queryset = GrandCompany.objects.annotate(num_characters=Count('characters')).all()
    
    @detail_route()
    def characters(self, request, pk=None, **kwargs):
        gc = self.get_object()
        viewset = CharacterViewSet(request=self.request, format_kwarg=self.format_kwarg)
        
        page = viewset.paginate_queryset(viewset.queryset.filter(gc_id=gc.id))
        serializer = viewset.get_serializer(page, many=True)
        return viewset.get_paginated_response(serializer.data)

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
    filter_fields = ('lodestone_id', 'first_name', 'last_name', 'server', 'title', 'race', 'clan', 'gender', 'gc', 'gc_rank', 'fc')
    search_fields = ('first_name', 'last_name')
    queryset = Character.objects.select_related('user').prefetch_related('levels', 'minions', 'mounts').all()
