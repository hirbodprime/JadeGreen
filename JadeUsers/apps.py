from django.apps import AppConfig


class JadeusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JadeUsers'
    def ready(self):
        import JadeUsers.signals



