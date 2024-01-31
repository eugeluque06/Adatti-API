from rest_framework.serializers import ModelSerializer
from AdattiAPI.models import adattiAPI,alimentos,categoria

class AdattiSerializer(ModelSerializer): 
    class Meta: 
        model = adattiAPI
        fields = ['id','title',]


class AlimentosSerializer(ModelSerializer): 
    class Meta: 
        model = alimentos
        fields = ['nombre','marca','RPNA','categoria','ingredientes','codigo_barras','tipo_alimento',]


class categoriaSerializer(ModelSerializer): 
    class Meta: 
        model = categoria
        fields = ['nombre',]
