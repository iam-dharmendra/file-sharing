"""
WSGI config for newwork project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newwork.settings')

application = get_wsgi_application()


# import os

# from django.core.wsgi import get_wsgi_application
# import socketio

# from socketio_app.views import sio

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network.settings")

# django_app = get_wsgi_application()
# application = socketio.WSGIApp(sio, django_app)




# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network.settings")

# # This application object is used by any WSGI server configured to use this
# # file. This includes Django's development server, if the WSGI_APPLICATION
# # setting points here.
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

