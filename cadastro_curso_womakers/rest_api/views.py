from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cursos.models import Curso
from rest_api.serializers import CursoModelSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'World API'})

class CursoModelViewSet(ModelViewSet):
    queryset = Curso.objects.all() # Esse queryset é o que vai ser retornado na API, lendo os dados dos cursos
    serializer_class = CursoModelSerializer # Esse serializer_class é o que vai ser retornado na API, lendo os dados dos cursos
