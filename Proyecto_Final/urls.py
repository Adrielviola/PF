from django.urls import path
from Proyecto_Final import views


urlpatterns = [
    path('estudiantes/', views.ListadoEstudiantes.as_view(), name='listado_estudiantes'),
    path('crear-estudiante/', views.CrearEstudiante.as_view(), name='crear_estudiante'),
    path('editar-estudiante/<int:pk>/', views.EditarEstudiante.as_view(), name='editar_estudiante'),
    path('eliminar-estudiante/<int:pk>/', views.EliminarEstudiante.as_view(), name='eliminar_estudiante'),
    path('mostrar-estudiante/<int:pk>/', views.MostrarEstudiante.as_view(), name='mostrar_estudiante'),
    path('cursos/', views.ListadoCursos.as_view(), name='listado_cursos'),
    path('crear-curso/', views.CrearCurso.as_view(), name='crear_curso'),
    path('editar-curso/<int:pk>/', views.EditarCurso.as_view(), name='editar_curso'),
    path('eliminar-curso/<int:pk>/', views.EliminarCurso.as_view(), name='eliminar_curso'),
    path('mostrar-curso/<int:pk>/', views.MostrarCurso.as_view(), name='mostrar_curso'),
    path('profesores/', views.ListadoProfesores.as_view(), name='listado_profesores'),
    path('crear-profesor/', views.CrearProfesor.as_view(), name='crear_profesor'),
    path('editar-profesor/<int:pk>/', views.EditarProfesor.as_view(), name='editar_profesor'),
    path('eliminar-profesor/<int:pk>/', views.EliminarProfesor.as_view(), name='eliminar_profesor'),
    path('mostrar-profesor/<int:pk>/', views.MostrarProfesor.as_view(), name='mostrar_profesor'),
    path('', views.home, name='home'),
    path('index/', views.home, name='home'),
]