
from rest_framework import serializers
from .models import Deporte, Federacion, Liga

class DeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deporte
        fields = '__all__'

class FederacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federacion
        fields = '__all__'

class LigaSerializer(serializers.ModelSerializer):
    deporte = DeporteSerializer(read_only=True)
    federacion = FederacionSerializer(read_only=True)
    deporte_id = serializers.PrimaryKeyRelatedField(
        queryset=Deporte.objects.all(), write_only=True, source='deporte'
    )
    federacion_id = serializers.PrimaryKeyRelatedField(
        queryset=Federacion.objects.all(), write_only=True, source='federacion'
    )

    class Meta:
        model = Liga
        fields = [
            'id', 'nombre', 'descripcion', 'deporte', 'deporte_id', 'federacion', 'federacion_id',
            'fecha_inicio', 'fecha_fin', 'estado'
        ]
