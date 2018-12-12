from rest_framework import serializers

from .models import RiskType, RiskTypeField, EnumOption


# Serializers for the models, for use by the REST API.

# One to many fields must be included, so that the serializer includes any
# "contained" data. They must also de define what serializer to use,
# and it must be marked as read_only, or they become required, which causes
# a catch 22 where you can't create anything.

class EnumOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnumOption
        fields = ('id', 'name', 'title', 'enum_field')


class RiskTypeFieldSerializer(serializers.ModelSerializer):
    # Define the relation as read_only, see above comment.
    options = EnumOptionSerializer(many=True, read_only=True)

    class Meta:
        model = RiskTypeField
        fields = ('id', 'title', 'description', 'field_type',
                  'required', 'options', 'risk_type')


class RiskTypeSerializer(serializers.ModelSerializer):
    # Define the relation as read_only, see above comment.
    type_fields = RiskTypeFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = ('id', 'title', 'description', 'type_fields')
