from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from caching.base import CachingManager, CachingMixin

class Race(CachingMixin, models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, unique=True)
    clan_1 = models.CharField(max_length=50)
    clan_2 = models.CharField(max_length=50, blank=True)
    
    objects = models.Manager()
    cached = CachingManager()
    
    def __unicode__(self):
        return self.name

class Server(CachingMixin, models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    objects = models.Manager()
    cached = CachingManager()
    
    def __unicode__(self):
        return self.name

class GrandCompany(CachingMixin, models.Model):
    class Meta:
        verbose_name_plural = u"grand companies"
    
    RANKS = [
        u"Recruit",
        u"{0} Private Third Class",
        u"{0} Private Second Class",
        u"{0} Private First Class",
        u"{0} Corporal",
        u"{0} Sergeant Third Class",
        u"{0} Sergeant Second Class",
        u"{0} Sergeant First Class",
        u"Chief {0} Sergeant",
        u"Second {0} Lieutenant",
    ]
    
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    short = models.CharField(max_length=10)
    
    objects = models.Manager()
    cached = CachingManager()
    
    def __unicode__(self):
        return self.name

class Job(CachingMixin, models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=3, blank=True)
    
    objects = models.Manager()
    cached = CachingManager()
    
    def __unicode__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name

class Minion(CachingMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    objects = models.Manager()
    cached = CachingManager()
    
    def __unicode__(self):
        return self.name

class Mount(CachingMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    objects = models.Manager()
    cached = CachingManager()
    
    def __unicode__(self):
        return self.name

class FreeCompany(models.Model):
    class Meta:
        verbose_name_plural = u"free companies"
    
    lodestone_id = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class Character(models.Model):
    GENDER_M = 1
    GENDER_F = 2
    GENDER_CHOICES = [ (GENDER_M, u"Male"), (GENDER_F, u"Female") ]
    
    lodestone_id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, related_name='characters', blank=True, null=True)
    
    server = models.ForeignKey(Server, related_name='characters')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.ForeignKey(Title, related_name='characters', blank=True, null=True)
    
    race = models.ForeignKey(Race, related_name='characters', null=True)
    clan = models.IntegerField(choices=[(1, u"First"), (2, u"Second")])
    gender = models.IntegerField(choices=GENDER_CHOICES)
    
    gc = models.ForeignKey(GrandCompany, verbose_name=u"Grand Company", related_name='characters', blank=True, null=True)
    gc_rank = models.IntegerField(u"Grand Company Rank", default=0)
    fc = models.ForeignKey(FreeCompany, verbose_name=u"Free Company", related_name='characters', blank=True, null=True)
    
    jobs = models.ManyToManyField(Job, through='Level')
    minions = models.ManyToManyField(Minion, related_name='characters')
    mounts = models.ManyToManyField(Mount, related_name='characters')
    
    attrs = JSONField(default={}, blank=True)
    
    def get_lodestone_url(self):
        return u"http://na.finalfantasyxiv.com/lodestone/character/{0}/".format(self.lodestone_id)
    
    def __unicode__(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

class Level(models.Model):
    character = models.ForeignKey(Character, related_name='levels')
    job = models.ForeignKey(Job, related_name='levels')
    level = models.IntegerField()
    exp_at = models.IntegerField()
    exp_of = models.IntegerField()
    
    def __unicode__(self):
        return u"{0} (Lv{1})".format(self.job.name, self.level)
