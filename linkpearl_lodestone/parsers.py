import requests
from bs4 import BeautifulSoup
from linkpearl_lodestone.models import Server, Title, Character

class BaseParser(object):
    USER_AGENT = u"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    
    model_class = None
    
    def get_url_for(self, id):
        raise NotImplemented
    
    def import_(self, id, obj=None, **kwargs):
        if not obj:
            obj = self.model_class(**kwargs)
        
        url = self.get_url_for(id)
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
    
    def get_url_for(self, id):
        return u"http://na.finalfantasyxiv.com/lodestone/character/{0}/".format(id)
    
    def save(self, soup, obj):
        name_box = soup.find(class_='player_name_txt').find('h2')
        name_link = name_box.find('a')
        
        id_s = filter(None, name_link['href'].split('/'))[-1]
        name_s = name_link.string
        title_s = name_box.find(class_='chara_title').string
        server_s = name_box.find('span').string[2:-1]
        
        obj.lodestone_id = int(id_s)
        obj.server = Server.objects.get_or_create(name=server_s)[0]
        obj.first_name, obj.last_name = name_s.split(' ')
        obj.title = Title.objects.get_or_create(name=title_s)[0]
        obj.save()
        
        return obj
