from google.appengine.api import urlfetch
import feedparser
import os

class RSSService:

    def posts_from(self, url):
        result = urlfetch.fetch(url)
        feed = feedparser.parse(result.content)
        posts = feed['entries'][0:3]
        return posts

    def materiais(self):
        ROOT_DIR = os.path.dirname(__file__)
        materiais = os.path.join(ROOT_DIR, 'materiais.xml')
        result = open(materiais, 'r')
        feed = feedparser.parse(result.read())
        items = feed['entries']
        return items