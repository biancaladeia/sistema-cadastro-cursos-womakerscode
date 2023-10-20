from django import forms
from cursos.models import Curso
from datetime import date, datetime, timezone

class CursoForm(forms.ModelForm):
    def clean_data_do_curso(self):
        data_do_curso = self.cleaned_data['data_do_curso']
        hoje = datetime.combine(date.today(), datetime.min.time()).astimezone(timezone.utc)
        
        if data_do_curso < hoje:
            raise forms.ValidationError('Não é possível cadastrar um curso nesta data!')
        return data_do_curso
    
    class Meta:
        model = Curso
        fields = ['titulo', 'nivel', 'carga_horaria', 'data_do_curso', 'descricao']
