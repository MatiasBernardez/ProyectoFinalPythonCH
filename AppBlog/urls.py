from django.urls import path
from django.contrib.auth.views import LogoutView
from AppBlog import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('unirse', views.unirse, name="unirse"),
    path('psicologo', views.inicio, name="psicologo"),
    path('especialidad', views.especialidad, name="especialidad"),
    path('modalidadatencion', views.modalidadatencion, name="modalidadatencion"),
    path('orientacion', views.orientacion, name="orientacion"),
    path('tipotratamiento', views.tipotratamiento, name="tipotratamiento"),
    path('zonaatencion', views.zonaatencion, name="zonaatencion"),
    #path('psicologoFormulario', views.psicologoFormulario, name="psicologoFormulario"),
    #path('busquedaNombrePsicologo', views.busquedaNombrePsicologo, name="busquedaNombrePsicologo"),
    path('buscar/', views.buscarzonaatencion),
    path('buscar1/', views.buscarmodalidadatencion),
    path('buscar2/', views.buscartipotratamiento),
    path('buscar3/', views.buscarorientacion),
    path('buscar4/', views.buscarespecialidad),
    path('leerPsicologos', views.leerPsicologos, name="leerPsicologos"),
    path('elminarPsicologo/<psicologo_nombre>', views.eliminarPsicologo, name="eliminarPsicologo"),
    path('editarPsicologo/<psicologo_nombre>', views.editarPsicologo, name="editarPsicologo"),
    path('psicologo/list', views.PsicologoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.PsicologoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PsicologoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PsicologoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PsicologoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    path('acercademi', views.acercademi, name="acercademi"),
]