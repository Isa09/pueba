from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiante/', include('estudiante.urls')),
    path('asignatura/', include('asignaturas.urls')),
]
