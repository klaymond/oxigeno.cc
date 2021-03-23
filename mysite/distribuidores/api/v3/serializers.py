import pytz
from datetime import datetime
from rest_framework import serializers
from distribuidores.models import Estado, Distribuidor, DistribuidorPotencial
from equipos.api.v3.serializers import ConcentradorSerializer, TanqueSerializer


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'nombre')


class DistribuidorSerializer(serializers.ModelSerializer):
    concentradores = serializers.SerializerMethodField()
    tanques = serializers.SerializerMethodField()
    lat = serializers.SerializerMethodField()
    lng = serializers.SerializerMethodField()
    ultima_actualizacion = serializers.SerializerMethodField()

    class Meta:
        model = Distribuidor
        fields = ('concentradores', 'tanques', 'id', 'horario', 'estado',
                  'direccion', 'ciudad', 'a_domicilio', 'pago_con_tarjeta',
                  'notas', 'telefono', 'ultima_actualizacion', 'lat', 'lng',
                  'whatsapp', 'link_pagina', 'nombre',
                  'abre_sabado', 'abre_domingo')

    def get_concentradores(self, obj):
        concentradores = obj.concentrador_set.all()
        return ConcentradorSerializer(instance=concentradores,
                                      many=True).data

    def get_tanques(self, obj):
        tanques = obj.tanque_set.all()
        return TanqueSerializer(instance=tanques, many=True).data

    def get_location(self, geo, position):
        return str(geo).split(',')[position]

    def get_lat(self, obj):
        return self.get_location(obj.geolocation, 0)

    def get_lng(self, obj):
        return self.get_location(obj.geolocation, 1)

    def get_ultima_actualizacion(self, obj):
        max_tanque = max(
            tanque.ultima_actualizacion for tanque in obj.tanque_set.all()) \
            if obj.tanque_set.all() else datetime.min.replace(tzinfo=pytz.UTC)
        max_concentrador = max(
            concentrador.ultima_actualizacion for concentrador in
            obj.concentrador_set.all()) if obj.concentrador_set.all() \
            else datetime.min.replace(tzinfo=pytz.UTC)
        ultima_actualización = max(
            [obj.ultima_actualizacion, max_tanque, max_concentrador])
        return ultima_actualización.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class HistoricalRecordSerializer(serializers.ModelSerializer):
    def __init__(self, model, *args, fields='__all__', **kwargs):
        self.Meta.model = model
        self.Meta.fields = fields
        super().__init__()

    class Meta:
        pass


class DistribuidorPotencialHistoricalSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = DistribuidorPotencial
        fields = '__all__'

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = '__all__'
        serializer = HistoricalRecordSerializer(model,
                                                obj.history.all().order_by(
                                                    'history_id'),
                                                fields=fields, many=True)
        serializer.is_valid()
        return serializer.data


class DistribuidorHistoricalSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Distribuidor
        fields = '__all__'

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = '__all__'
        serializer = HistoricalRecordSerializer(model,
                              obj.history.all().order_by('history_id'),
                              fields=fields, many=True)
        serializer.is_valid()
        return serializer.data


class DistribuidorUpdateSerializer(serializers.Serializer):
    distribuidorId = serializers.IntegerField()
    estadoId = serializers.IntegerField()
    notas = serializers.CharField()
    notasInternas = serializers.CharField()
    tanqueOfreceRenta = serializers.BooleanField()
    tanqueDisponibilidadRenta = serializers.IntegerField()
    tanqueOfreceVenta = serializers.BooleanField()
    tanqueDisponibilidadVenta = serializers.IntegerField()
    tanqueOfreceRecarga = serializers.BooleanField()
    tanqueDisponibilidadRecarga = serializers.IntegerField()
    concentradorOfreceRenta = serializers.BooleanField()
    concentradorDisponibilidadRenta = serializers.IntegerField()
    concentradorOfreceVenta = serializers.BooleanField()
    concentradorDisponibilidadVenta = serializers.IntegerField()

    def validate(self, attrs):
        self.distribuidor_data = {
            "notas": attrs['notas'],
            "notas_internas": attrs['notasInternas'],
            "estado_id": attrs['estadoId']
        }
        self.tanque_data = {
            "ofrece_renta": attrs['tanqueOfreceRenta'],
            "disponibilidad_renta": attrs['tanqueDisponibilidadRenta'],
            "ofrece_venta": attrs['tanqueOfreceVenta'],
            "disponibilidad_venta": attrs['tanqueDisponibilidadVenta'],
            "ofrece_recarga": attrs['tanqueOfreceRecarga'],
            "disponibilidad_recarga": attrs['tanqueDisponibilidadRecarga']
        }
        self.concentrador_data = {
            "ofrece_renta": attrs['concentradorOfreceRenta'],
            "disponibilidad_renta": attrs['concentradorDisponibilidadRenta'],
            "ofrece_venta": attrs['concentradorOfreceVenta'],
            "disponibilidad_venta": attrs['concentradorDisponibilidadVenta'],
        }
        try:
            self.distribuidor = Distribuidor.objects.filter(
                id=attrs['distribuidorId'])
            if not self.distribuidor:
                raise serializers.ValidationError('distribuidor no encontrado')
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return super().validate(attrs)


class DistribuidorPotencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistribuidorPotencial
        fields = '__all__'
        read_only_fields = ('id',)