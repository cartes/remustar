from django.apps import AppConfig

class GestionRemustarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion_remustar'

    def ready(self):
        import remustar.signals  # Carga las señales al iniciar la aplicación
