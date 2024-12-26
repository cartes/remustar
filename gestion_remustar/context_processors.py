from django.contrib.auth.models import Group
from gestion_remustar.models import Business

def is_admin_or_superadmin(request):
    if request.user.is_authenticated:
        is_admin = request.user.groups.filter(name='Administrador').exists() or request.user.is_superuser

    else:
        is_admin = False

    return {'is_admin_or_superadmin': is_admin}

def have_businesses(request):
    return {'have_businesses': Business.objects.exists()}