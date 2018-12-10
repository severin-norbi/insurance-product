from rest_framework import serializers

from .models import RiskType, RiskTypeField, EnumOption


class EnumOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnumOption
        fields = ('id', 'name', 'title', 'enum_field')


class RiskTypeFieldSerializer(serializers.ModelSerializer):
    options = EnumOptionSerializer(many=True, read_only=True)

    class Meta:
        model = RiskTypeField
        fields = ('id', 'title', 'description', 'field_type',
                  'required', 'options', 'risk_type')


class RiskTypeSerializer(serializers.ModelSerializer):
    type_fields = RiskTypeFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = ('id', 'title', 'description', 'type_fields')
