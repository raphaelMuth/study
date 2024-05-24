from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from ..models import MyModel
from ..serializers.mymodelserializer import MyModelSerializer

class MyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer