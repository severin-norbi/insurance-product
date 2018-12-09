from django.http import HttpResponse
from django.views import generic
from rest_framework import viewsets

from . import models, serializers


# TODO: Class based view
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class RiskTypeIndexView(generic.ListView):
    model = models.RiskType


class RiskTypeDetailView(generic.DetailView):
    model = models.RiskType


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RiskTypes to be viewed or edited.
    """
    queryset = models.RiskType.objects.all()
    serializer_class = serializers.RiskTypeSerializer


class RiskTypeFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RiskTypeFields to be viewed or edited.
    """
    queryset = models.RiskTypeField.objects.all()
    serializer_class = serializers.RiskTypeFieldSerializer


class EnumOptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EnumOptions to be viewed or edited.
    """
    queryset = models.EnumOption.objects.all()
    serializer_class = serializers.EnumOptionSerializer
