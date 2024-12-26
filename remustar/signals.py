from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    admin_group, created = Group.objects.get_or_create(name='Administrador')
    user_group, created = Group.objects.get_or_create(name='Usuario')

    if created:
        admin_permissions = Permission.objects.all()
        admin_group.permissions.set(admin_permissions)

        user_permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
        user_group.permissions.set(user_permissions)