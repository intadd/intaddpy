import os




import sys



from django.core.wsgi import get_wsgi_application



path=os.path.abspath(__file__+'/../..')

sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
#application=django.core.handlers.wsgi.WSGIHandler()
