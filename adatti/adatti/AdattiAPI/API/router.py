from rest_framework.routers import DefaultRouter
from AdattiAPI.API.view import adatiApiViewSet,alimentoApiViewSet,categoriaApiViewSet

routers_adatti = DefaultRouter()
routers_alimentos = DefaultRouter()
routers_categoria = DefaultRouter()

routers_adatti.register(prefix='adatti',basename='adatti',viewset=adatiApiViewSet)

routers_alimentos.register(prefix='alimentos',basename='alimentos',viewset=alimentoApiViewSet)

routers_categoria.register(prefix='categoria',basename='categoria',viewset=categoriaApiViewSet)
