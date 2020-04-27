"""
WSGI config for bae project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bae.settings')

application = get_wsgi_application()

# whitenoise options commented out because of version incompatibility.
#from whitenoise.django import DjangoWhiteNoise
#application = DjangoWhiteNoise(application)
