from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Q
import random
import json
from gestion_remustar.forms import BusinessForm
from gestion_remustar.models import Business, BusinessMeta, Configuration
from collections import defaultdict

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser, login_url='home')(view_func)

@superuser_required
def business_list(request):
    businesses = Business.objects.all()
    return render(request, 'gestion_remustar/business/business_list.html', {
        'businesses': businesses,
        'title': 'Lista de empresas'
        })

@superuser_required
def business_create(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save()
            messages.success(request, 'Empresa creada correctamente')
            return redirect('business_list')
    else:
        form = BusinessForm()

    return render(request, 'gestion_remustar/business/business_create.html', {'businessForm': form, 'title': 'Crear empresa'})

@superuser_required
def business_card(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'gestion_remustar/business/business_card.html', {
        'business': business,
        'title': f'Empresa {business.name}'
        })
    
@superuser_required
def business_update(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    metadata = BusinessMeta.objects.filter(business_id=business)
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            business = form.save()
            messages.success(request, 'Empresa actualizada correctamente')
            return redirect('business_card', business_id=business.id)
    
    return render(request, 'gestion_remustar/business/business_card.html', {
        'business': business,
        'metadata': metadata,
        'title': f'Empresa {business.name}'
    })
    
# vista para la mutualidad del negocio, que esta guardada en tabla business Meta
@superuser_required
def business_mutualidad(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    
    if request.method == 'POST':
        mutual = request.POST.get('mutual')
        ccaf = request.POST.get('ccaf')
        
        BusinessMeta.objects.update_or_create(
            business_id=business, key='mutual', defaults={'value': mutual}
        )
        BusinessMeta.objects.update_or_create(
            business_id=business, key='ccaf', defaults={'value': ccaf}
        )
        
        messages.success(request, 'Datos actualizados correctamente')
        return redirect('business_mutualidad', business_id=business.id)
    else:
        # Obtener datos de mutual y CCAF
        mutual = BusinessMeta.objects.filter(business_id=business.id, key='mutual').first()
        ccaf = BusinessMeta.objects.filter(business_id=business_id, key='ccaf').first()

        mutual_value = mutual.value if mutual else None
        ccaf_value = ccaf.value if ccaf else None
            
        list_ccaf_value = _get_ccaf() 
        list_mutual_value = _get_mutualidades()

    return render(request, 'gestion_remustar/business/business_mutualidad.html', {
        'business': business,
        'mutual': mutual_value,
        'ccaf': ccaf_value,
        'list_ccaf': list_ccaf_value,
        'list_mutual': list_mutual_value,
        'title': f'Mutualidad de {business.name}'
    })
 
def _get_ccaf():
    list_ccaf = Configuration.objects.get(Q(key='ccaf_list'))
    if isinstance(list_ccaf.value, str):
        list_ccaf_value = json.loads(list_ccaf.value)
    elif isinstance(list_ccaf.value, list):
        list_ccaf_value = list_ccaf.value
    else:
        raise TypeError("list_ccaf.value debe ser JSON válido o una lista")
    
    return list_ccaf_value
 
def _get_mutualidades():
    list_mutual = Configuration.objects.get(Q(key='mutualidades_list'))
    if isinstance(list_mutual.value, str):
        list_mutual_value = json.loads(list_mutual.value)
    elif isinstance(list_mutual.value, list):
        list_mutual_value = list_mutual.value
    else:
        raise TypeError("list_mutual.value debe ser JSON válido o una lista")
    
    return list_mutual_value