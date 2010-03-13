from google.appengine.ext import webapp
import view
from rss.rss_service import RSSService

class IndexHandler(webapp.RequestHandler):
    def get(self):
        rsss = RSSService()
        posts = rsss.posts_from("http://visaoagil.wordpress.com/feed/")
        msgs = rsss.posts_from("http://rss.groups.yahoo.com/group/visaoagil/rss")
        page = view.Page()
        page.render(self, 'templates/index/index.html', {'posts':posts, 'msgs':msgs})

class EdicoesHandler(webapp.RequestHandler):
    def get(self):
        page = view.Page()
        page.render(self, 'templates/index/edicoes.html')

class ContatoHandler(webapp.RequestHandler):
    def get(self):
        page = view.Page()
        page.render(self, 'templates/index/contato.html')

class InscricaoHandler(webapp.RequestHandler):
    def get(self):
        page = view.Page()
        page.render(self, 'templates/index/inscricao.html')

class BibliotecaHandler(webapp.RequestHandler):
    def get(self):
        rsss = RSSService()
        items = rsss.materiais()

        page = view.Page()
        page.render(self, 'templates/index/biblioteca.html', {'items':items})
