from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Crea un superusuario si no existe"

    def handle(self, *args, **options):
        User = get_user_model()

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='front_242',
                email='cristiancartesa@gmail.com'
            )

            self.stdout.write(self.style.SUCCESS('Superusuario creado con éxito'))
        else:
            self.stdout.write(self.style.SUCCESS('El superusuario ya existe'))
