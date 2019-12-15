from django.db import models

# Clases relacionadas con la app de Rescatados.
class Adoptante(models.Model):
    run = models.CharField(blank= True, max_length= 10,primary_key=True, verbose_name= 'Run')
    nombre = models.CharField(blank= True, max_length= 30, null= False,  verbose_name= 'Nombre')
    apellido = models.CharField(blank= True, max_length= 30, null= False, verbose_name= 'Apellido')
    direccion = models.CharField(blank= True, max_length= 50, null= False, verbose_name= 'Dirección')
    ciudad = models.CharField(blank= True, max_length= 30, null= False, verbose_name= 'Ciudad')
    telefono = models.IntegerField(blank= True, null= False, verbose_name= 'Telefono')
    correo = models.EmailField(blank= True, max_length= 50, null= False,verbose_name= 'Correo')

class Meta:
    verbose_name = 'Adoptante'
    verbose_name_plural = 'Adoptantes'
    ordering = ['nombre']

def __str__(self):
    return self.nombre 


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombreM = models.CharField(blank= True, max_length= 20, null= False,  verbose_name= 'Nombre Mascota')
    tipo_roedor = models.CharField(blank= True, max_length= 20, null= False, verbose_name= 'Tipo de Roedor')
    ciudadM = models.CharField(blank= True, max_length= 30, null= False, verbose_name= 'Cuidad')
    infoM = models.TextField(blank= True, max_length= 100, null= True,verbose_name= 'Información')


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key= True)
    run_adop = models.ForeignKey(Adoptante, on_delete = models.CASCADE)
    fecha = models.DateField('Fecha Adopción', blank = False, null = False)
    mascota_adop = models.OneToOneField(Mascota, on_delete = models.CASCADE)


