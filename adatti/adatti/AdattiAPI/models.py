from django.db import models

# Create your models here.

class adattiAPI(models.Model): 
    title = models.CharField(max_length = 255)
    content = models.TextField()


class categoria(models.Model): 
    nombre = models.CharField(max_length = 50)
    icono = models.ImageField(upload_to="") #no funcionara hasta que no este creado el html entre comillas hay que poner de donde va a traer la foto

class alimentos(models.Model): 
    nombre = models.CharField(max_length = 255)
    marca = models.CharField(max_length = 100)
    RPNA = models.CharField(max_length = 100)  #puede ser que nos de error al introducir los datos 
    categoria =  models.ForeignKey(categoria, on_delete=models.CASCADE) #tiene que modificarse en cascada
    ingredientes = models.CharField(max_length = 255)
    codigo_barras = models.CharField(max_length = 10)
    tipo_alimento = models.CharField(max_length = 10)
