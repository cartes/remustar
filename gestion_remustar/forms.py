from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Business

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name',  'email', 'phone_number', 'address', 'password1', 'password2', 'id_business')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone_number': 'Número de teléfono',
            'address': 'Dirección',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'first_name': forms.TextInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'phone_number': forms.TextInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'address': forms.TextInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'password1': forms.PasswordInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'password2': forms.PasswordInput(attrs={'class': 'input input-sm input-bordered w-full'}),
            'id_business': forms.Select(attrs={'class': 'input input-sm input-bordered w-full'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar los widgets de password1 y password2
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input input-sm input-bordered w-full'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input input-sm input-bordered w-full'})
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'


class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone_number': 'Número de teléfono',
            'address': 'Dirección'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full'}),
            'first_name': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'phone_number': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'address': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'rut', 'description', 'address', 'phone_number', 'email', 'website')
        labels = {
            'name': 'Nombre',
            'rut': 'RUT',
            'description': 'Descripción',
            'address': 'Dirección',
            'phone_number': 'Número de teléfono',
            'email': 'Correo electrónico',
            'website': 'Sitio web'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'rut': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'description': forms.Textarea(attrs={'class': 'input input-bordered w-full'}),
            'address': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'phone_number': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full'}),
            'website': forms.URLInput(attrs={'class': 'input input-bordered w-full'}),
        }