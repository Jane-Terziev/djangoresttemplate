from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

celery_app = Celery('tasks', broker=os.environ.get("REDIS_URL", default='redis://localhost:6379/0'))
celery_app.conf.update(
    CELERYD_MAX_TASKS_PER_CHILD=1,
    CELERYD_WORKER_CONCURRENCY=1,
    CELERYD_PREFETCH_MULTIPLIER=1,
    CELERY_ACKS_LATE=True,
)


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
