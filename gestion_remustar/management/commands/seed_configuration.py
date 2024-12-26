from django.core.management.base import BaseCommand
from gestion_remustar.models import Configuration
import json

class Command(BaseCommand):
    help = "Seed de configuración"
    
    def handle(self, *args, **options):
        ccaf = [
            {'name': 'Caja de Compensación Los Andes', 'code': 'CCAF-LANDES'},
            {'name': 'Caja de Compensación Los Héroes', 'code': 'CCAF-LHEROES'},
            {'name': 'Caja de Compensación La Araucana', 'code': 'CCAF-LARAU'},
            {'name': 'Caja de Compensación 18 de Septiembre', 'code': 'CCAF-18SEP'},
        ]
        
        config_key = 'ccaf_list'
        config, created = Configuration.objects.update_or_create(
            key=config_key,
            defaults={'value': ccaf}
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Configuración "{config_key}" creada.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Configuración "{config_key}" actualizada.'))
            
        mutualidades = [
            {"name": "Mutual de Seguridad CChC", "code": "MUTUAL-CCHC"},
            {"name": "Asociación Chilena de Seguridad", "code": "ACHS"},
            {"name": "Instituto de Seguridad del Trabajo", "code": "IST"},
            {"name": "Instituto de Seguridad Laboral", "code": "ISL"}
        ]

        config_key = 'mutualidades_list'
        config, created = Configuration.objects.update_or_create(
            key=config_key,
            defaults={'value': mutualidades}
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Configuración "{config_key}" creada.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Configuración "{config_key}" actualizada.'))