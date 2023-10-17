from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    html = '''
    <!DOCTYPE html>
        <head>
            <title>Cursos Online</title>
        </head>
        <body>
            <h1> Olá mundo!</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)



def cadastro(request):
    pass

