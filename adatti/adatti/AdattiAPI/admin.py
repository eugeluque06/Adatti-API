from django.contrib import admin
from AdattiAPI.models import adattiAPI,alimentos,categoria
# Register your models here.

@admin.register(adattiAPI)
class Adatti_Admin(admin.ModelAdmin): 
    list_display = ['id','title']


@admin.register(categoria)
class categoria(admin.ModelAdmin): 
    list_display = ['nombre']


@admin.register(alimentos)
class alimento(admin.ModelAdmin): 
    list_display = ['nombre','marca','RPNA','categoria','ingredientes','codigo_barras','tipo_alimento']