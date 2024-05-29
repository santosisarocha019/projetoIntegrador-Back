import django_filters
from app_smart.models import Sensor, TemperaturaData
from rest_framework import permissions
from app_smart.api import serializers
from rest_framework.views import APIView
from django.db.models import Q


class SensorFilter(django_filters.FilterSet):
    responsavel = django_filters.CharFilter(field_name='responsavel', lookup_expr='icontains')
    status_operacional = django_filters.CharFilter(field_name='status_operacional', lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='exact')
    localizacao = django_filters.CharFilter(field_name='localizacao', lookup_expr='icontains')

    class Meta:
        model = Sensor
        fields = ['status_operacional', 'tipo', 'localizacao', 'responsavel']


class TemperaturaDataFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id',None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(valor__get=sensor_id)
        if valor_gte:
            filters &= Q(valor__get=valor_gte)
        if valor_lt:
            filters &= Q(valor__get=valor_lt)
        if timestamp_gte:
            filters &= Q(valor__get=timestamp_gte)
        if timestamp_lt:
            filters &= Q(valor__get=timestamp_lt)

        queryset = TemperaturaData.objects.filter(filters)
        serializer = serializers.TemperaturaDataSerializer(queryset, many =True)
        return Response(serializers.data)
    
class TemperaturaDataFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    timestamp_lte= django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')
    sensor = django_filters.NumberFilter(field_name='sensor')
    valor_gte = django_filters.NumberFilter(field_name='valor', lookup_expr='gte')
    valor_lte = django_filters.NumberFilter(field_name='valor', lookup_expr='lte')

    class Meta:
        model = TemperaturaData
        fields = ['timestamp_gte', 'timestamp_lte', 'sensor', 'valor_gte', 'valor_lte']

