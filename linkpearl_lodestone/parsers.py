import requests
from bs4 import BeautifulSoup
from linkpearl_lodestone.models import Race, Server, Title, Character

class BaseParser(object):
    USER_AGENT = u"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    
    model_class = None
    
    def get_url_for(self, obj):
        raise NotImplemented
    
    def import_(self, **kwargs):
        obj = self.model_class(**kwargs)
        return self.update(obj)
    
    def update(self, obj):
        url = self.get_url_for(obj)
        html = self.fetch(url)
        soup = self.consume(html)
        return self.save(soup, obj)
    
    def fetch(self, url):
        r = requests.get(url, headers={ 'User-Agent': self.USER_AGENT })
        r.raise_for_status()
        return r.text
    
    def consume(self, html):
        return BeautifulSoup(html, "lxml")
    
    def save(self, soup, obj):
        raise NotImplemented

class CharacterParser(BaseParser):
    model_class = Character
    
    def get_url_for(self, obj):
        return u"http://na.finalfantasyxiv.com/lodestone/character/{0}/".format(obj.lodestone_id)
    
    def save(self, soup, obj):
        name_box = soup.find(class_='player_name_txt').find('h2')
        name_link = name_box.find('a')
        race_box = soup.find(class_='chara_profile_title')
        
        id_s = filter(None, name_link['href'].split('/'))[-1]
        name_s = name_link.string
        title_s = name_box.find(class_='chara_title').string
        server_s = name_box.find('span').string[2:-1]
        race_s, clan_s, gender_s = race_box.string.split(' / ')
        
        obj.lodestone_id = int(id_s)
        obj.server = Server.objects.get_or_create(name=server_s)[0]
        obj.first_name, obj.last_name = name_s.split(' ')
        obj.title = Title.objects.get_or_create(name=title_s)[0]
        
        obj.race = Race.objects.get_or_create(name=race_s, defaults={ 'clan_1': clan_s })[0]
        obj.clan = 1 if clan_s == obj.race.clan_1 else 2
        if obj.clan == 2 and not obj.race.clan_2:
            obj.race.clan_2 = clan_s
            obj.race.save()
        obj.gender = Character.GENDER_M if gender_s == u'\u2642' else Character.GENDER_F
        
        obj.save()

        return obj
