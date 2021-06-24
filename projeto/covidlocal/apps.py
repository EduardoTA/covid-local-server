from django.apps import AppConfig

class CovidlocalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'covidlocal'
    def ready(self):
        pass
