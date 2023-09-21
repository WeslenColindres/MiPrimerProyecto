from django.urls import path, include
from . import views

urlpatterns = [
    path('lista/', views.listar, name='listar'),

    # URLs para pais
    path('pais/agregar/', views.agregar_pais, name='agregar_pais'),
    path('pais/editar/<int:pk>/', views.actualizar_pais, name='pais_edit'),
    path('pais/eliminar/<int:pk>/', views.eliminar_pais, name='pais_delete'),
    
     # URLs para Departamento
    path('departamentos/agregar/', views.agregar_departamento, name='agregar_dep'),
    path('departamentos/editar/<int:pk>/', views.actualizar_departamento, name='actualizar_dep'),
    path('departamentos/eliminar/<int:pk>/', views.eliminar_departamento, name='dep_delete'),
    
    # URLs para Municipio
    path('municipios/agregar/', views.agregar_municipio, name='agregar_municipio'),
    path('municipios/editar/<int:pk>/', views.actualizar_municipio, name='actualizar_municipio'),
    path('municipio/eliminar/<int:pk>/', views.eliminar_municipio, name='municipio_delete'),
    
    #URLs usuario
    path('usuarios/', views.Usuario.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:user_id>/permisos/', views.Usuario.editar_permisos_usuario, name='editar_permisos_usuario'),
    
    #URLs secion
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('',views.home_view, name='base'),
    
    path('api/', include('catalogo.urls_api')),
]
