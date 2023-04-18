# pylint: skip-file
import getpass
import shlex
from subprocess import PIPE  # nosec

import psutil
from django.core.management.base import BaseCommand
from django.utils.autoreload import run_with_reloader


def restart_celery():
    for proc in psutil.process_iter():
        if proc.username() != getpass.getuser():  # skip processes not owned by user
            continue
        if proc.name() != "celery":
            continue
        if not proc.children():
            continue
        celery_proc = proc  # found parent celery process
        celery_proc.terminate()
        break
    cmd = "celery -A backend worker -l info"
    psutil.Popen(shlex.split(cmd), stdout=PIPE)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Starting celery worker with autoreload")
        run_with_reloader(restart_celery)
