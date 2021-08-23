import os

import sys

sys.path.append('/opt/bitnami/projects/ana')

os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/ana/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ana.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
