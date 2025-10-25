# Esse arquivo configura o WSGI para o projeto Latinder.
# WSGI (Web Server Gateway Interface) é uma especificação para servidores web e aplicações Python
# que permite comunicação síncrona
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'latinder_proj.settings')

application = get_wsgi_application()
