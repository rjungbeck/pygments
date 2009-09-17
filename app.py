from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class App(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(open('README', 'r').read())
  def post(self):
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(pygmentize(self.request.get("lang"), self.request.get("code")))

application = webapp.WSGIApplication([('/', App)], debug=True)

def pygmentize(lang, code):
  lexer = get_lexer_by_name(lang, stripall=True)
  formatter = HtmlFormatter(linenos=False, cssclass="pygments_appspot")
  return highlight(code, lexer, formatter)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
