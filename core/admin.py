from django.contrib import admin

from .models import *


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'cargo',
        'ativo',
        'modificado',
    )


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = (
        'servico',
        'icone',
        'ativo',
        'modificado'
    )


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cargo',
        'ativo',
        'modificado',
    )


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'icone',
        'ativo',
        'modificado',
    )
