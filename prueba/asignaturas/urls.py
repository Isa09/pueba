

from django.urls import path
from .views import aginatura_, eliminar_asignatura,registar_asignatura, clases

app_name = 'agnatura'

urlpatterns = [
    path('',aginatura_.as_view(),name = 'asignatura'),
    path('clase/',clases.as_view(),name = 'clase'),
    path('registrar-asignatura/', registar_asignatura),
    path('eliminar/asignatura/<int:pk>',eliminar_asignatura)
    # path('', estudiant, name = 'Estudiante'),
]
