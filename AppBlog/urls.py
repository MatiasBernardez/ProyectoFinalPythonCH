from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
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
]