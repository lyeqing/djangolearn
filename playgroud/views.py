#from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.views
# # Create your views here.

# def say(request):
#     return HttpResponse('Hello' )
# def createPerson(request, person):
#     return HttpResponse('Hello' )
# import os
# import sys
# file_dir = os.path.dirname(__file__)
# sys.path.append(file_dir)
from rest_framework import viewsets
from playgroud.modelss import Persons, Activities
from playgroud.serializes import  ActivitySerializer,PersonSerializer


class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activities.objects.all()
	serializer_class = ActivitySerializer


class PersonViewSet(viewsets.ModelViewSet):
	queryset = Persons.objects.all()
	serializer_class = PersonSerializer