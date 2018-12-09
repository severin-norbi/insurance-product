from django.contrib import admin

from .models import RiskType, RiskTypeField

admin.site.register(RiskType)
admin.site.register(RiskTypeField)
