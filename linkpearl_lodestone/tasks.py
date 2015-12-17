from __future__ import absolute_import
from celery import shared_task
from linkpearl_lodestone.models import Character
from linkpearl_lodestone.parsers import CharacterParser

@shared_task
def update_character(**kwargs):
    character = Character.objects.get(**kwargs)
    parser = CharacterParser()
    parser.update(character)
