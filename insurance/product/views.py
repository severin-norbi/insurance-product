from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets

from .models import RiskType, RiskTypeField
from .serializers import RiskTypeSerializer, RiskTypeFieldSerializer


# TODO: Class based view
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class RiskTypeIndexView(generic.ListView):
    model = RiskType


class RiskTypeDetailView(generic.DetailView):
    model = RiskType


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RiskType to be viewed or edited.
    """
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer

class RiskTypeFieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RiskType to be viewed or edited.
    """
    queryset = RiskTypeField.objects.all()
    serializer_class = RiskTypeFieldSerializer
