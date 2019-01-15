# myapp/apps.py
from django.apps import AppConfig


class CoreAppConfig(AppConfig):

    name = 'app'

    def ready(self):
        import app.signals