from getfvco import application
from google.appengine.ext.webapp.util import run_wsgi_app

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()