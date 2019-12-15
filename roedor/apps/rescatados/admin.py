from django.contrib import admin
from .models import Adoptante
from .models import Mascota
from .models import Ficha

# Registrar Adoptantes, Mascotas y Fichas.
admin.site.register(Adoptante)
admin.site.register(Mascota)
admin.site.register(Ficha)
