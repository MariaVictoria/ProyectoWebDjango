from django.shortcuts import render
from  rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer
# Create your views here.


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset= Programmer.objects.all()  #ORM
    serializer_class = ProgrammerSerializer