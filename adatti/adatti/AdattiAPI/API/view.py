from rest_framework.viewsets import ModelViewSet
from  AdattiAPI.models import adattiAPI,alimentos
from AdattiAPI.API.serializers import AdattiSerializer, AlimentosSerializer,categoriaSerializer


class adatiApiViewSet(ModelViewSet): 
    serializer_class = AdattiSerializer
    queryset = adattiAPI.objects.all()


class alimentoApiViewSet(ModelViewSet): 
    serializer_class = AlimentosSerializer
    queryset = alimentos.objects.all()

class categoriaApiViewSet(ModelViewSet): 
    serializer_class = categoriaSerializer
    queryset = alimentos.objects.all()