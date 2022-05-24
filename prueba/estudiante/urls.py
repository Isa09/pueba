

from django.urls import path
from .views import estudiant, eliminar_estudiante,registar_estudiante

app_name = 'estudiante'

urlpatterns = [
    path('',estudiant.as_view(),name = 'Estudiante'),
    path('registrar-estudiante/', registar_estudiante),
    path('eliminar/estudiante/<int:pk>',eliminar_estudiante)
    # path('', estudiant, name = 'Estudiante'),
]
