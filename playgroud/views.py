#from django.shortcuts import render
import json
from django.http import HttpResponse
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
from sqlalchemy import create_engine
from rest_framework import viewsets
from playgroud.modelss import Persons, Activities
from playgroud.serializes import  ActivitySerializer,PersonSerializer
from sqlalchemy import text
def say(request):
    server = 'localhost'
    database = 'DjangoLearnData'
    username = 'louis'
    password = '$Cc123456'
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        result = conn.execute(text("select * from playgroud_persons"))
        rows = result.fetchall()
        #date = json.load(result)
        print(rows[0].email)
        #print(result[0])
    return HttpResponse('Hello' )
class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activities.objects.all()
	serializer_class = ActivitySerializer


class PersonViewSet(viewsets.ModelViewSet):
	queryset = Persons.objects.all()
	serializer_class = PersonSerializer