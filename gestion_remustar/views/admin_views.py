from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout, get_user_model
from gestion_remustar.forms import CustomUserCreationForm, CustomUserEditForm
from gestion_remustar.models import Business, CustomUserMeta

@login_required
@permission_required('auth.add_user', raise_exception=True)

def user_list(request):
    User = get_user_model()  # Obtiene el modelo de usuario

    admin_group = Group.objects.get(name='Administrador')
    users = User.objects.filter(groups=admin_group).exclude(id=request.user.id)

    return render(request, 'gestion_remustar/user_list.html', {
        'users': users,
        'title': 'Lista de administradores'
    })

def create_admin(request):
    businesses = _get_businesses()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            position = request.POST.get('position')
            user = form.save()

            user_group, created = Group.objects.get_or_create(name='Administrador')
            user.groups.add(user_group)
            
            if (position):
                CustomUserMeta.objects.create(user_id=user, key='position', value=position)
                

            messages.success(request, 'Administrador creado exitosamente.')
            return redirect('admin_list')  # Redirige a la lista de usuarios después de la creación
    else:
        form = CustomUserCreationForm()

    return render(request, 'gestion_remustar/admin_create.html', {
        'form': form,
        'businesses': businesses,
        })

def _get_businesses():
    businesses = Business.objects.all()
    return businesses