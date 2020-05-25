import os
from django.core.wsgi import get_wsgi_application

# Change djangoresttemplate to the new project name
environment = os.environ.get('ENVIRONMENT')
if environment == 'develop':
    config = 'djangoresttemplate.settings.develop'
elif environment == 'staging':
    config = 'djangoresttemplate.settings.staging'
elif environment == 'production':
    config = 'djangoresttemplate.settings.production'
else:
    config = 'djangoresttemplate.settings.base'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config)

application = get_wsgi_application()