web: gunicorn djangoresttemplate.asgi:application -k uvicorn.workers.UvicornWorker
worker: celery -A djangoresttemplate worker -l info
release: python manage.py migrate