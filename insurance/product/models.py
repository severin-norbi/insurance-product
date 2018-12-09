from django.db import models


FIELD_REGISTRY = (
    ('text', 'A short text string'),
    ('number', 'A number'),
    ('date', 'A date'),
    ('enum', 'A choice in a list'),
)


class RiskType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class RiskTypeField(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE,
                                  related_name='type_fields')
    title = models.CharField(max_length=50)
    description = models.TextField()
    field_type = models.CharField(max_length=10, choices=FIELD_REGISTRY)
    required = models.BooleanField()
