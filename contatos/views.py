from django.shortcuts import render, get_object_or_404
from .models import Contato



# pega os dados e retorna pro html
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', { 'contatos': contatos }) 


def detalhes_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/detalhes_contato.html', { 
        'contato': contato }) 

