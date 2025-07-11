"""
WSGI config for phi_mart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phi_mart.settings')

app = get_wsgi_application()

# vercel.json file configuration

# // {
# //     "builds": [{
# //       "src": "phi_mart/wsgi.py",
# //       "use": "@vercel/python",
# //       "config": { "maxLambdaSize": "15mb", "runtime": "python3.11.3" }
# //     }],
# //     "routes": [
# //       {
# //         "src": "/(.*)",
# //         "dest": "phi_mart/wsgi.py"
# //       }
# //     ]
# // }
