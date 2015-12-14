from django.contrib import admin
from linkpearl_lodestone.models import Server, Title, Character

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'server', 'title')
