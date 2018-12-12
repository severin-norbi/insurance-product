from django.db import models


# This is the list of field types. It's currently hard coded.
FIELD_REGISTRY = (
    ('text', 'A short text string'),
    ('number', 'A number'),
    ('date', 'A date'),
    ('enum', 'A choice in a list'),
)


class RiskType(models.Model):
    """A type of risk with dynamically created schema"""
    title = models.CharField(max_length=50)
    description = models.TextField()


class RiskTypeField(models.Model):
    """Fields in RiskType schemas"""
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE,
                                  related_name='type_fields')
    title = models.CharField(max_length=50)
    description = models.TextField()
    field_type = models.CharField(max_length=10, choices=FIELD_REGISTRY)
    required = models.BooleanField()


class EnumOption(models.Model):
    """Options for enum fields"""
    enum_field = models.ForeignKey(RiskTypeField, on_delete=models.CASCADE,
                                   related_name='options')
    # This is the value that is stored
    name = models.CharField(max_length=50)
    # This is the display value
    title = models.CharField(max_length=50)
