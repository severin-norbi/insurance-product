from rest_framework import serializers
from .models import RiskType, RiskTypeField


class RiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskType
        fields = ('id', 'title', 'description', 'type_fields')


class RiskTypeFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskTypeField
        fields = ('id', 'title', 'description', 'risk_type', 'field_type', 'required')
