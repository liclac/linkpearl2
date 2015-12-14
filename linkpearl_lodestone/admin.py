from django.contrib import admin
from linkpearl_lodestone.models import Server, Title, Character
from linkpearl_lodestone.parsers import CharacterParser

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'server', 'title')
    actions = ['update']
    
    def update(self, request, queryset):
        p = CharacterParser()
        for char in queryset:
            p.update(char)
