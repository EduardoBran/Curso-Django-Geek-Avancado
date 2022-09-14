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

@admin.register(NamePrice)
class NamePriceAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'ativo',
        'modificado',
    )
    
@admin.register(TotalUsuarios)
class TotalUsuariosAdmin(admin.ModelAdmin):
    list_display = (
        'total',
        'ativo',
        'modificado',
    )

@admin.register(TotalArmazenamento)
class TotalArmazenamentoAdmin(admin.ModelAdmin):
    list_display = (
        'total',
        'ativo',
        'modificado',
    )

@admin.register(Suporte)
class SuporteAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'ativo',
        'modificado',
    )

@admin.register(Atualizacao)
class AtualizacaoAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'ativo',
        'modificado',
    )

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'preco',
        'suporte',
        'ativo',
        'modificado',
    )
