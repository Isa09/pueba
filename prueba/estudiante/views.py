from django.shortcuts import render,redirect
from .models import estudiante
from django.views.generic import CreateView

# def estudiant(request):
#     data = {
#         'titulo': 'Gestor estudiante',
#         'estudiante': estudiante.objects.all()
#     }
#     return render(request,'estudiante.html',data)

class estudiant(CreateView):
    model = estudiante
    template_name = 'estudiante.html'
    fields ='__all__'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['titulo'] = 'Gestion estudiante'
        contex['estudiante'] = estudiante.objects.all()
        return contex

def registar_estudiante(request):

    nombre = request.POST['txtNombre']
    print(nombre)
    apellido = request.POST['txtApellido']
    identificacion = request.POST['numIdentificacion']
    email = request.POST['txtEmail']
    programa = request.POST['txtPrograma']
    estudiant = estudiante.objects.create(nombre=nombre, apellido=apellido,identificacion=identificacion,
                                          correo=email,p_academico=programa)

    return redirect('estudiante:Estudiante')

def eliminar_estudiante(request,pk):
    estudiante.objects.filter(pk=pk).delete()
    return redirect('estudiante:Estudiante')