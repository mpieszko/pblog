from django.db import models
from django.utils import timezone


# Create your models here.

#---Noticia
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80,null=False)
    subtitulo = models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True)
    imagen = models.ImageField(null=True,blank=True,upload_to='noticia',default='noticia/notidefault.png')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)
    
    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()

#--- Tabla para los contactos:
opciones_consultas=[
    [0,'consulta'],
    [1,'reclamo'],
    [2,'sugerencia'],
    [3,'felicitaciones'],
]
class Contacto(models.Model):
    nombre= models.CharField(max_length=50)
    correo = models.EmailField(max_length=80)
    tipo_de_consulta = models.IntegerField(choices= opciones_consultas, default='0')
    mensaje = models.TextField()
    desea_recibir_avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
#---
