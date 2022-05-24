
from django.shortcuts import render,redirect
from .models import asignatura, clase,estudiante
from django.views.generic import CreateView

# def estudiant(request):
#     data = {
#         'titulo': 'Gestor estudiante',
#         'estudiante': estudiante.objects.all()
#     }
#     return render(request,'estudiante.html',data)

class aginatura_(CreateView):
    model = asignatura
    template_name = 'asignatura.html'
    fields ='__all__'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['titulo'] = 'Gestion asignatura'
        contex['asignatura'] = asignatura.objects.all()
        return contex



def registar_asignatura(request):
    nombre = request.POST['txtNombre']
    salon = request.POST['txtSalon']
    horario = request.POST['txtHoratio']
    id_profesor = request.POST['nunIdeprofesor']
    estudiant = asignatura.objects.create(nombre=nombre, salon=salon,horario=horario,id_profesor=id_profesor)

    return redirect('agnatura:asignatura')

def eliminar_asignatura(request,pk):
    asignatura.objects.filter(pk=pk).delete()
    return redirect('agnatura:asignatura')

# clases
class clases(CreateView):
    model = clase
    template_name = 'curso.html'
    fields ='__all__'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['titulo'] = 'Gestion clases'
        contex['curso'] = clase.objects.all()
        contex['estudiante'] = estudiante.objects.all()
        contex['asignatura'] = asignatura.objects.all()
        return contex

def registar_clase(request):
    nombre = request.POST['txtNombre']
    salon = request.POST['txtSalon']
    horario = request.POST['txtHoratio']
    id_profesor = request.POST['nunIdeprofesor']
    estudiant = clase.objects.create(nombre=nombre, salon=salon,horario=horario,id_profesor=id_profesor)

    return redirect('agnatura:asignatura')

def eliminar_clase(request,pk):
    clase.objects.filter(pk=pk).delete()
    return redirect('agnatura:asignatura')