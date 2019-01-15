"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
#import sys
#sys.path.append('/var/www/devfameghino')
#sys.path.append('/usr/local/lib/python2.7/dist-packages/')

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()
ALLOWED_HOSTS = ['.fameghino.com.ar/','http://127.0.0.1']