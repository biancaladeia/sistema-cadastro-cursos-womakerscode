from django.db import models

# Create your models here.
class Curso(models.Model):
    niveis_de_curso = (
        ('Iniciante', 'Iniciante'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado') # fixed the tuple index
    )    
    titulo = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50, choices=niveis_de_curso) # fixed the parenthesis
    carga_horaria = models.IntegerField()
    data_do_curso = models.DateTimeField(help_text='aaaa/mm/dd')
    descricao = models.TextField()
    
    def __str__(self):
        return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'
    
    class Meta:
        verbose_name = 'Cadastro de Curso'
        verbose_name_plural = 'Cadastro de Cursos'
        ordering = ['data_do_curso']
    
    