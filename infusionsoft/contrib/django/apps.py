import os

from django.apps import AppConfig

from infusionsoft.contrib.django.initialize import initialize


class InfusionsoftAppConfig(AppConfig):
    name = 'infusionsoft'
    verbose_name = 'Infusionsoft'
    path = os.path.join(os.path.dirname(__file__), '__init__.py')

    def ready(self):
        initialize()
