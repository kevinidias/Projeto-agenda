from django.contrib import admin

# Register your models here.
from .models import Categoria, Contato



class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria_fk')
    list_display_links = ('nome', 'sobrenome') # vira link
    list_filter = ('data_criacao', 'nome')
    list_per_page = 15


admin.site.register(Contato, ContatoAdmin)


admin.site.register(Categoria)