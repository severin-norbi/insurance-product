from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import RiskType, RiskTypeField, EnumOption


class EnumOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnumOption
        fields = ('id', 'name', 'title', 'enum_field')


class RiskTypeFieldSerializer(serializers.HyperlinkedModelSerializer):
    options = EnumOptionSerializer(many=True)

    class Meta:
        model = RiskTypeField
        fields = ('id', 'title', 'description', 'field_type',
                  'required', 'options', 'risk_type')



class RiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    type_fields = RiskTypeFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = ('id', 'title', 'description', 'type_fields')
