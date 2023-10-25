# def test_config():
#    assert 1 == 1

from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo = 'Java', 
        data_do_curso = date.today(), 
        carga_horaria = '40'
    )
    return curso

@pytest.mark.django_db #decorador para criar um banco de dados para teste
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Java: 2023-10-25 - 40'