from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Curso, Estudiante, Profesor
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render


def home(request):
    return render(request, 'Proyecto_Final/index.html')


class ListadoCursos(ListView):
    model = Curso
    template_name = 'Proyecto_Final/listar_curso.html'


class CrearCurso(CreateView):
    model = Curso
    template_name = 'Proyecto_Final/crear_curso.html'
    success_url = reverse_lazy('listado_cursos')
    fields = '__all__'


class EditarCurso(UpdateView):
    model = Curso
    template_name = 'Proyecto_Final/editar_curso.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_curso', kwargs={'pk':self.object.pk})


class EliminarCurso(DeleteView):
    model = Curso
    template_name = 'Proyecto_Final/eliminar_curso.html'
    success_url = reverse_lazy('listado_cursos')

class MostrarCurso(DetailView):
    model = Curso
    template_name = 'Proyecto_Final/mostrar_curso.html'

class ListadoEstudiantes(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'Proyecto_Final/listar_estudiante.html'


class CrearEstudiante(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Estudiante
    permission_required = "estudiante.add_estudiante"
    template_name = 'Proyecto_Final/crear_estudiante.html'
    success_url = reverse_lazy('listado_estudiantes')
    fields = '__all__'


class EditarEstudiante(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Estudiante
    permission_required = "estudiante.change_estudiante"
    template_name = 'Proyecto_Final/editar_estudiante.html'
    fields = '__all__'

def get_success_url(self) -> str:
    return reverse_lazy('mostrar_estudiante', kwargs={'pk':self.object.pk})


class EliminarEstudiante(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Estudiante
    permission_required = "estudiante.delete_estudiante"
    template_name = 'Proyecto_Final/eliminar_estudiante.html'
    success_url = reverse_lazy('listado_estudiantes')

class MostrarEstudiante(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = 'Proyecto_Final/mostrar_estudiante.html'

class ListadoProfesores(ListView):
    model = Profesor
    template_name = 'Proyecto_Final/listar_profesor.html'


class CrearProfesor(CreateView):
    model = Profesor
    template_name = 'Proyecto_Final/crear_profesor.html'
    success_url = reverse_lazy('listado_profesores')
    fields = '__all__'


class EditarProfesor(UpdateView):
    model = Profesor
    template_name = 'Proyecto_Final/editar_profesor.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_profesor', kwargs={'pk':self.object.pk})


class EliminarProfesor(DeleteView):
    model = Profesor
    template_name = 'Proyecto_Final/eliminar_profesor.html'
    success_url = reverse_lazy('listado_profesores')

class MostrarProfesor(DetailView):
    model = Profesor
    template_name = 'Proyecto_Final/mostrar_profesor.html'



