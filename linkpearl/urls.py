"""linkpearl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from linkpearl_lodestone.views import RaceViewSet, ServerViewSet, GrandCompanyViewSet, JobViewSet, TitleViewSet, MinionViewSet, MountViewSet, FreeCompanyViewSet, CharacterViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'races', RaceViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'grand-companies', GrandCompanyViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'minions', MinionViewSet)
router.register(r'mounts', MountViewSet)
router.register(r'free-companies', FreeCompanyViewSet)
router.register(r'characters', CharacterViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
