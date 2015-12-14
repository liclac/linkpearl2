from django import forms
from django.contrib import admin
from linkpearl_lodestone.models import Race, Server, Title, Character
from linkpearl_lodestone.parsers import CharacterParser

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        obj = kwargs.get('instance', None)
        if obj:
            self.fields['clan'].choices = [
                (1, obj.race.clan_1),
                (2, obj.race.clan_2 or "???"),
            ]

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'server', 'title', 'race', 'clan_str', 'gender')
    actions = ['update']
    form = CharacterForm
    
    def clan_str(self, obj):
        return obj.race.clan_1 if obj.clan == 1 else obj.race.clan_2 or "???"
    clan_str.admin_order_field = 'clan'
    clan_str.short_description = u"Clan"
    
    def update(self, request, queryset):
        p = CharacterParser()
        for char in queryset:
            p.update(char)
