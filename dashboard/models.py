from django.db import models

# Create your models here.
class CentroEsportivos(models.Model):
    nome = models.CharField(max_length=100)
    data_entrada = models.DateField()
    
    def __str__(self):
        return f"{self.nome}  Entrou no dia: {self.data_entrada}"


class Agendamentos(models.Model):
    
    centro_esportivo = models.ForeignKey(CentroEsportivos, on_delete=models.CASCADE)
    agendamentos_dia = models.IntegerField(default=0)
    agendamentos_semana = models.IntegerField(default=0)
    agendamentos_mes = models.IntegerField(default=0)
    agendamentos_ano = models.IntegerField(default=0)
    
    cancelamento_dia = models.IntegerField(default=0)
    cancelamento_semana = models.IntegerField(default=0)
    cancelamento_mes = models.IntegerField(default=0)
    cancelamento_ano = models.IntegerField(default=0)

    def __str__(self):
        return f"Agendamentos - Dia: {self.agendamentos_dia}, Semana: {self.agendamentos_semana}, Mês: {self.agendamentos_mes}, Ano: {self.agendamentos_ano}"

class Faturamento(models.Model):
    
    centro_esportivo = models.ForeignKey(CentroEsportivos, on_delete=models.CASCADE)
    dia = models.DecimalField(max_digits=10, decimal_places=2)
    semana = models.DecimalField(max_digits=10, decimal_places=2)
    mes = models.DecimalField(max_digits=10, decimal_places=2)
    ano = models.DecimalField(max_digits=10, decimal_places=2)
    
    dia_previsto = models.DecimalField(max_digits=10, decimal_places=2)
    semana_previsto = models.DecimalField(max_digits=10, decimal_places=2)
    mes_previsto = models.DecimalField(max_digits=10, decimal_places=2)
    ano_previsto = models.DecimalField(max_digits=10, decimal_places=2)

    pg_pix = models.DecimalField(max_digits=10, decimal_places=2)
    pg_local = models.DecimalField(max_digits=10, decimal_places=2)
    pg_cartão = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.centro_esportivo)

class AgendamentoDiaSemana(models.Model):

    centor_esportivo = models.ForeignKey(CentroEsportivos, on_delete=models.CASCADE)
    segunda = models.IntegerField(default=0)
    terca = models.IntegerField(default=0)
    quarta = models.IntegerField(default=0)
    quinta = models.IntegerField(default=0)
    sexta = models.IntegerField(default=0)
    sabado = models.IntegerField(default=0)
    domingo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.sabado)

    
class Cliente(models.Model):
    
    semana_choices =(
        ('SEG', 'Segunda'),
        ('TER', 'Terca'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'SEX'),
        ('SAB', 'Sabado'),
        ('DOM', 'Domingo'),
    )


    novo_cliente = models.CharField(max_length=20)
    semana = models.CharField(max_length=3, choices=semana_choices)
        
    def __str__(self):
        return f"Cliente: {self.novo_cliente}"
 