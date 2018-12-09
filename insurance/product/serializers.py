from rest_framework import serializers
from .models import RiskType, RiskTypeField, EnumOption


class EnumOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnumOption
        fields = ('id', 'name', 'title')


class RiskTypeFieldSerializer(serializers.HyperlinkedModelSerializer):
    options = EnumOptionSerializer(many=True)

    class Meta:
        model = RiskTypeField
        fields = ('id', 'title', 'description', 'field_type',
                  'required', 'options')


class RiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    type_fields = RiskTypeFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = ('id', 'title', 'description', 'type_fields')
