from django.urls import path,include
from . import views
from .api.viewsets import CreateUserAPIViewSet, SensorViewSet, TemperaturaDataViewSet, UmidadeDataViewSet, LuminosidadeDataViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .api.filters import SensorFilterView, TemperaturaDataFilterView, UmidadeDataFilterView, LuminosidadeDataFilterView


router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura',TemperaturaDataViewSet)
router.register(r'umidade',UmidadeDataViewSet)
router.register(r'Luminosidade',LuminosidadeDataViewSet)


urlpatterns = [   
    path('', views.abre_index, name='abre_index'),
    path('api/create_user', CreateUserAPIViewSet.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/sensor_filter/', SensorFilterView.as_view(), name='sensor_filter'),
    path('api/temperatura_filter/', TemperaturaDataFilterView.as_view(), name='temperatura_filter'),
    path('api/umidade_filter/', UmidadeDataFilterView.as_view(), name='umidade_filter'),
    path('api/luminosidade_filter/', LuminosidadeDataFilterView.as_view(), name='luminosidade_filter'),



]