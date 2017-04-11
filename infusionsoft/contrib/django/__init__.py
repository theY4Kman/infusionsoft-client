import django

from infusionsoft.contrib.django.initialize import initialize


default_app_config = 'infusionsoft.contrib.django.apps.InfusionsoftAppConfig'


if django.VERSION < (1, 7):
    # Pre-1.7, there is no AppConfig.ready, so we must initialize here
    initialize()
