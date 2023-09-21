from django.shortcuts import render, redirect, get_object_or_404
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from django.contrib.auth.models import User, Permission
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.

# def listar(request):
#         query = request.GET.get('search', '')
#         action = request.GET.get('action')
        
#         paises = Pais.objects.filter(Q(nombre__icontains=query)) if query else Pais.objects.all()
        
#         departamentos = Departamento.objects.filter(Q(nombre__icontains=query)) if query else Departamento.objects.all()
        
#         municipios = Municipio.objects.filter(Q(nombre__icontains=query)) if query else Municipio.objects.all()

#         if action == 'buscar' and query:
#             paises = paises.filter(Q(nombre__icontains=query)) #
        
#         elif action == 'listar':
#             query =''

#         context = {
#             'paises': paises,
#             'departamentos': departamentos,
#             'municipios': municipios,
#             'query': query
#         }

#         return render(request, 'listar.html', context)
def listar(request):
    query = request.GET.get('search', '')
    action = request.GET.get('action')
    
    context = {
        'resultados': [],
        'query': query,
        'stado': True,
    }
    
    if action == 'buscar' and query:
    # Buscamos por países
        for pais in Pais.objects.filter(Q(nombre__icontains=query) & Q(status=context['stado'])):
            context['resultados'].append({'id': pais.id,'pais': pais.nombre, 'status': pais.status, 'departamentos': []})

        # Buscamos por departamentos
        for depto in Departamento.objects.filter(Q(nombre__icontains=query) & Q(status=context['stado'])):
            pais_entry = next((entry for entry in context['resultados'] if entry['pais'] == depto.pais.nombre), None)
            if not pais_entry:
                pais_entry = {'pais': depto.pais.nombre, 'departamentos': []}
                context['resultados'].append(pais_entry)
            pais_entry['departamentos'].append({ 'id': depto.id, 'departamento': depto.nombre, 'municipios': []})

        # Buscamos por municipios
        for municipio in Municipio.objects.filter(Q(nombre__icontains=query) & Q(status=context['stado'])):
            pais_entry = next((entry for entry in context['resultados'] if entry['pais'] == municipio.departamento.pais.nombre), None)
            if not pais_entry:
                pais_entry = {'id': municipio.departamento.pais.id, 'pais': municipio.departamento.pais.nombre, 'departamentos': []}
                context['resultados'].append(pais_entry)
                
            depto_entry = next((entry for entry in pais_entry['departamentos'] if entry['departamento'] == municipio.departamento.nombre), None)
            if not depto_entry:
                depto_entry = {'id':municipio.departamento.id, 'departamento': municipio.departamento.nombre, 'municipios': []}
                pais_entry['departamentos'].append(depto_entry)
                
            depto_entry['municipios'].append({'id': municipio.id, 'nombre': municipio.nombre})

    elif action == 'listar':
        # Listamos todos los países
        for pais in Pais.objects.filter(status = context['stado']):
            context['resultados'].append({'id': pais.id, 'pais': pais.nombre,'status': pais.status, 'departamentos': []})

        # Listamos todos los departamentos
        for depto in Departamento.objects.filter(status = context['stado']):
            pais_entry = next((entry for entry in context['resultados'] if entry['pais'] == depto.pais.nombre), None)
            if not pais_entry:
                pais_entry = {'id': depto.pais.id, 'pais': depto.pais.nombre,'status': depto.pais.status, 'departamentos': []}
                context['resultados'].append(pais_entry)
            pais_entry['departamentos'].append({ 'id': depto.id, 'departamento': depto.nombre, 'status': depto.status, 'municipios': []})

        # Listamos todos los municipios
        for municipio in Municipio.objects.filter(Q(nombre__icontains=query) & Q(status=context['stado'])):
            pais_entry = next((entry for entry in context['resultados'] if entry['pais'] == municipio.departamento.pais.nombre), None)
            if not pais_entry:
                pais_entry = {'id': municipio.departamento.pais.id,'pais': municipio.departamento.pais.nombre,'status': municipio.departamento.pais.status, 'departamentos': []}
                context['resultados'].append(pais_entry)
                
            depto_entry = next((entry for entry in pais_entry['departamentos'] if entry['departamento'] == municipio.departamento.nombre), None)
            if not depto_entry:
                depto_entry = {'id': municipio.departamento.id, 'departamento': municipio.departamento.nombre, 'status': municipio.departamento.status, 'municipios': []}
                pais_entry['departamentos'].append(depto_entry)
                
            depto_entry['municipios'].append({'id': municipio.id, 'nombre': municipio.nombre, 'status': municipio.status})
        
    else :   
        # Listamos todos los países
        for pais in Pais.objects.filter(status = context['stado']):
            context['resultados'].append({'id': pais.id, 'pais': pais.nombre, 'status': pais.status, 'departamentos': []})

        # Listamos todos los departamentos
        for depto in Departamento.objects.filter(status = context['stado']):
            pais_entry = next((entry for entry in context['resultados'] if entry['pais'] == depto.pais.nombre), None)
            if not pais_entry:
                pais_entry = {'id': depto.pais.id, 'pais': depto.pais.nombre, 'departamentos': []}
                context['resultados'].append(pais_entry)
            pais_entry['departamentos'].append({ 'id': depto.id, 'departamento': depto.nombre, 'municipios': []})

        # Listamos todos los municipios
        for municipio in Municipio.objects.filter(Q(nombre__icontains=query) & Q(status=context['stado'])):
            pais_entry = next((entry for entry in context['resultados'] if entry['pais'] == municipio.departamento.pais.nombre), None)
            if not pais_entry:
                pais_entry = {'id': municipio.departamento.id,'pais': municipio.departamento.pais.nombre, 'departamentos': []}
                context['resultados'].append(pais_entry)
                
            depto_entry = next((entry for entry in pais_entry['departamentos'] if entry['departamento'] == municipio.departamento.nombre), None)
            if not depto_entry:
                depto_entry = {'id': municipio.departamento.id, 'departamento': municipio.departamento.nombre, 'municipios': []}
                pais_entry['departamentos'].append(depto_entry)
                
            depto_entry['municipios'].append({'id': municipio.id, 'nombre': municipio.nombre})

        
    paginator = Paginator(context['resultados'], 10)
    page = request.GET.get('page')

    try:
        resultados_paginados = paginator.page(page)
    except PageNotAnInteger:
       
        resultados_paginados = paginator.page(1)
    except EmptyPage:
        
        resultados_paginados = paginator.page(paginator.num_pages)

    context['resultados'] = resultados_paginados

    return render(request, 'listar.html', context)
    



@permission_required('catalogo.add_pais', raise_exception=True)
def     agregar_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar", mode='lista')
    
    else:
        form = PaisForm()
        
    return render(request, 'paises/form.html', {'form':form})

@permission_required('catalogo.change_pais', raise_exception=True)
def actualizar_pais(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            return redirect('listar', mode='lista')
    else:
        form = PaisForm(instance=pais)
    return render(request, 'paises/form.html', {'form': form, 'object': pais})

@permission_required('catalogo.delete_pais', raise_exception=True)
def eliminar_pais(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        pais.delete()
        print(pais)
        return redirect('listar')
    return render(request, 'paises/eliminar.html', {'pais': pais.nombre, 'puede_eliminar': pais.puede_eliminar})
    
        

@permission_required('catalogo.add_departamento', raise_exception=True)
def agregar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar', mode='lista')  
    else:
        form = DepartamentoForm()
        
    return render(request, 'departamento/form.html', {'form': form})

@permission_required('catalogo.change_departamento', raise_exception=True)
def actualizar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('listar', mode='lista')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departamento/form.html', {'form': form, 'object': departamento})

@permission_required('catalogo.delete_departamento', raise_exception=True)
def eliminar_departamento(request, pk,):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar')
    return render(request, 'departamento/eliminar.html', {'departamento': departamento.nombre})



@permission_required('catalogo.add_municipio', raise_exception=True)
def agregar_municipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar', mode='lista') 
    else:
        form = MunicipioForm()
        
    return render(request, 'municipios/form.html', {'form': form})

@permission_required('catalogo.change_municipio', raise_exception=True)
def actualizar_municipio(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == 'POST':
        form = MunicipioForm(request.POST, instance=municipio)
        if form.is_valid():
            form.save()
            return redirect('listar', mode='lista')
    else:
        form = MunicipioForm(instance=municipio)
    return render(request, 'municipios/form.html', {'form': form, 'object': municipio})

@permission_required('catalogo.delete_municipio', raise_exception=True)
def eliminar_municipio(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == 'POST':
        municipio.delete()
        return redirect('listar')
    return render(request, 'municipios/eliminar.html', {'municipio': municipio.nombre})



def home_view(request):
    return render(request, 'base.html')

class Usuario:
    def lista_usuarios(request):
        usuarios = User.objects.all()
        return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})

    def editar_permisos_usuario(request, user_id):
        usuario = User.objects.get(pk=user_id)
        

        if request.method == 'POST':
            # Obtener permisos desde el formulario
            permisos_form = request.POST.getlist('permisos')

            # Limpiar permisos actuales
            usuario.user_permissions.clear()

            # Asignar nuevos permisos
            for permiso_id in permisos_form:
                permiso = Permission.objects.get(pk=permiso_id)
                usuario.user_permissions.add(permiso)

            return redirect('lista_usuarios')

        permisos = Permission.objects.all()
        permisos_actuales = usuario.user_permissions.all()
        context = {
        'usuario': usuario, 
        'permisos': permisos, 
        'permisos_actuales': permisos_actuales
    }

        return render(request, 'usuario/editar_permisos.html', context)
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'secion/register.html'
    success_url = reverse_lazy('login')  
        
class MyLoginView(LoginView):
    template_name = 'secion/login.html'