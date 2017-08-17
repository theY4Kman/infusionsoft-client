from django.conf import settings


def initialize():
    """Initialize the client from Django settings once"""
    import infusionsoft

    if not infusionsoft.is_initialized:
        api_key = getattr(settings, 'INFUSIONSOFT_API_KEY', None)

        app_name = getattr(settings, 'INFUSIONSOFT_APP_NAME', None)
        if app_name:
            app_name_or_api_url = app_name
        else:
            app_name_or_api_url = getattr(settings, 'INFUSIONSOFT_API_URL',
                                          None)

        if not api_key or not app_name_or_api_url:
            raise ValueError(
                'Please set INFUSIONSOFT_APP_NAME or INFUSIONSOFT_API_URL, '
                'and INFUSIONSOFT_API_KEY in your settings')

        options = getattr(settings, 'INFUSIONSOFT_CLIENT_OPTIONS', {})
        infusionsoft.initialize(app_name_or_api_url, api_key, **options)
