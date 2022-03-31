from django.apps import AppConfig


class ReferalConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'referal'

    def ready(self):
        import referal.signals