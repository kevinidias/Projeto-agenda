from django.shortcuts import render
from .models import Contato



# pega os dados e retorna pro html
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', { 'contatos': contatos }) 


