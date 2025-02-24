from django.contrib import admin
from .models import Senha

@admin.register(Senha)
class SenhaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data_criacao')
    ordering = ('-data_criacao',)  # Ordena da mais recente para a mais antiga
    search_fields = ('valor',)  # Adiciona um campo de busca

