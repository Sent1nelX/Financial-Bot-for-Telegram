from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Телеграмм Ботяра'

    def ready(self) -> None:
        import main.signals