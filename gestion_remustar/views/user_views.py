from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout, get_user_model
from gestion_remustar.forms import CustomUserCreationForm, CustomUserEditForm
from gestion_remustar.models import Business

# Create your views here.
@login_required
@permission_required('auth.add_user', raise_exception=True)
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.groups.add(Group.objects.get(name='Usuario'))
            return redirect('users_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'gestion_remustar/register_user.html', {'form': form})

def user_list(request):
    User = get_user_model()  # Obtiene el modelo de usuario
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'gestion_remustar/user_list.html', {
        'users': users,
        'title': 'Lista de usuarios'
    })

def user_detail(request, user_id):
    User = get_user_model()  # Obtiene el modelo de usuario
    user = User.objects.get(id=user_id)
    return render(request, 'gestion_remustar/user_detail.html', {
        'user': user,
        'title': f'Detalle de {user.username}'
    })

def user_edit(request, user_id):
    User = get_user_model()  # Obtiene el modelo de usuario
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)  # Cargar datos del formulario
        if form.is_valid():
            form.save()  # Guarda todos los campos del formulario
            messages.success(request, 'La información del usuario ha sido actualizada correctamente.')
            return redirect('user_detail', user_id=user.id)
    else:
        form = CustomUserEditForm(instance=user)  # Carga el formulario con los datos del usuario existente

    return render(request, 'gestion_remustar/user_edit.html', {
        'user': user,
        'form': form,
        'title': f'Editar {user.username}'
    })

def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            user_group, created = Group.objects.get_or_create(name='Usuario')
            user.groups.add(user_group)

            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('users_list')  # Redirige a la lista de usuarios después de la creación
    else:
        form = CustomUserCreationForm()

    return render(request, 'gestion_remustar/user_create.html', {'form': form})    

def user_delete(request, user_id):
    User = get_user_model()  # Obtiene el modelo de usuario
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('users_list')

    return render(request, 'gestion_remustar/user_delete.html', {
        'user': user,
        'title': f'Eliminar {user.username}'
    })

def have_businesses(request):
    return Business.objects.exists()

def login_view(request):
    # Redirige al usuario autenticado directamente a la lista de usuarios
    if request.user.is_authenticated:
        return redirect('users_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if have_businesses(request):
                return redirect('users_list')
            else:
                return redirect('business_list')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')  
            
    return render(request, 'gestion_remustar/home.html', {
        'title': 'Remustar | Iniciar sesión'
    })

def logout_view(request):
    logout(request)
    return redirect('home')