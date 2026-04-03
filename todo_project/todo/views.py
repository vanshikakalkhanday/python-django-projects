from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Todo

from .serializers import TodoSerializer

from django_filters.rest_framework import DjangoFilterBackend

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()

    serializer_class = TodoSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['completed']
 