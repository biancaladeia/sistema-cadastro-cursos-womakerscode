from rest_framework.serializers import ModelSerializer
from cursos.models import Curso

class CursoModelSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # Retorna todos os campos do model Curso
        


