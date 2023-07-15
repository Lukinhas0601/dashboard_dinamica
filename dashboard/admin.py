from django.contrib import admin
from .models import CentroEsportivos, Agendamentos, Faturamento, AgendamentoDiaSemana, Cliente

class AgendamentosInline(admin.TabularInline):
    model = Agendamentos

class FaturamentoInline(admin.TabularInline):
    model = Faturamento

class AgendamentoDiaSemanaInline(admin.TabularInline):
    model = AgendamentoDiaSemana

@admin.register(CentroEsportivos)
class CentroEsportivosAdmin(admin.ModelAdmin):
    inlines = [AgendamentosInline,
               FaturamentoInline, 
               AgendamentoDiaSemanaInline]

admin.site.register(Agendamentos)
admin.site.register(Faturamento)
admin.site.register(AgendamentoDiaSemana)
admin.site.register(Cliente)
