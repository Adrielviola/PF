from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Carreras, Corredores
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render


def home(request):
    return render(request, 'Proyecto_Final/index.html')


class ListadoCarreras(ListView):
    model = Carreras
    template_name = 'Proyecto_Final/listado_carreras.html'


class CrearCarreras (LoginRequiredMixin,CreateView,PermissionRequiredMixin):
    model = Carreras
    template_name = 'Proyecto_Final/crear_carreras.html'
    success_url = reverse_lazy('crear_carreras')
    fields = '__all__'


class EditarCarreras(UpdateView):
    model = Carreras
    template_name = 'Proyecto_Final/editar_carreras.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_carreras', kwargs={'pk':self.object.pk})


class EliminarCarreras(DeleteView):
    model = Carreras
    template_name = 'Proyecto_Final/eliminar_carreras.html'
    success_url = reverse_lazy('listado_carreras')

class MostrarCarreras(ListView):
    model = Carreras
    template_name = 'Proyecto_Final/mostrar_carreras.html'

class ListadoCorredores(LoginRequiredMixin, ListView):
    model = Corredores
    template_name = 'Proyecto_Final/listar_corredores.html'


class CrearCorredores(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Corredores
    permission_required = "corredor.add_corredor"
    template_name = 'Proyecto_Final/crear_corredores.html'
    success_url = reverse_lazy('listado_corredores')
    fields = '__all__'


class EditarCorredores(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Corredores
    permission_required = "corredor.change_corredor"
    template_name = 'Proyecto_Final/editar_corredores.html'
    fields = '__all__'

def get_success_url(self) -> str:
    return reverse_lazy('mostrar_ecorredores', kwargs={'pk':self.object.pk})


class EliminarCorredores(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Corredores
    permission_required = "corredor.delete_corredor"
    template_name = 'Proyecto_Final/eliminar_corredores.html'
    success_url = reverse_lazy('listado_corredores')

class MostrarCorredores(LoginRequiredMixin, DetailView):
    model = Corredores
    template_name = 'Proyecto_Final/mostrar_corredores.html'

