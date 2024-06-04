from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import *

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta :
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs ={'password':{'write_only': True}}

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class TemperaturaDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaData
        fields = '__all__'

class UmidadeDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = UmidadeData
        fields = '__all__'

class LuminosidadeDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = LuminosidadeData
        fields = '__all__'

class ContadorDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContadorData
        fields = '__all__'