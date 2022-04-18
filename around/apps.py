from django.apps import AppConfig


class AroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'around'

    def ready(self):
        import around.signals


