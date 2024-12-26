"""
URL configuration for remustar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion_remustar.views import user_views, app_views, admin_views, business_views

urlpatterns = [
    path('', app_views.home, name='home'),  # URL para la ruta base
    path('register/', user_views.register_user, name='register_user'),
    path('users/', user_views.user_list, name='users_list'),
    path('users/<int:user_id>/', user_views.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit/', user_views.user_edit, name='user_edit'),
    path('users/create', user_views.user_create, name='user_create'),
    path('users/<int:user_id>/delete/', user_views.user_delete, name='user_delete'),
    path("login/", user_views.login_view, name="login"),
    path('logout/', user_views.logout_view, name='logout'),

    # URL para la ruta creacion de administradores
    path('admin/', admin_views.user_list, name='admin_list'),
    path('create_admin/', admin_views.create_admin, name='admin_create'),

    # URL para la ruta de creacion de negocios
    path('business/', business_views.business_list, name='business_list'),
    path('business/create/', business_views.business_create, name='business_create'),
    path('business/<int:business_id>/', business_views.business_card, name='business_card'),
    path('business/<int:business_id>/update/', business_views.business_update, name='business_update'),
    path('business/<int:business_id>/mutualidad/', business_views.business_mutualidad, name='business_mutualidad'),
    
    #Ruta ejemplo uso modelo de IA
    #path('model/', business_views.model, name='model'),
]
