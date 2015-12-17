from __future__ import absolute_import
from requests import HTTPError
from celery import shared_task
from linkpearl_lodestone.models import Character
from linkpearl_lodestone.parsers import CharacterParser

@shared_task
def import_character(**kwargs):
    # Ignore attempts to reimport tasks
    try:
        Character.objects.get(**kwargs)
        return False
    except Character.DoesNotExist:
        pass
    
    character = Character(**kwargs)
    parser = CharacterParser()
    try:
        character = parser.update(character)
        return character.id if character else None
    except HTTPError:
        pass

@shared_task
def update_character(**kwargs):
    character = Character.objects.get(**kwargs)
    parser = CharacterParser()
    try:
        character = parser.update(character)
        return character.id if character else None
    except HTTPError:
        pass

@shared_task
def import_next_batch_of_characters(num):
    last_unclaimed = Character.objects.filter(user=None).order_by('lodestone_id').last()
    last_lid = int(last_unclaimed.lodestone_id) if last_unclaimed else 0
    
    first = last_lid + 1
    last = first + num
    
    for lid in reversed(xrange(first, last)):
        import_character.delay(lodestone_id=lid)
    
    return (first, last)
