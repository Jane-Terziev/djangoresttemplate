#!/usr/bin/env python
import os
import sys


def main():
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
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
