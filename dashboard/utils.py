#============= Função dos Filtros ============
def month_filter(month):
    if month == 0:
        mask = df['Mês'].isin(df['Mês'].unique())
    else:
        mask = df['Mês'].isin([month])
    return mask 

def team_filter(team):
    if team == 0:
        mask = df['Equipe'].isin(df['Equipe'].unique())
    else:
        mask = df['Equipe'].isin([team])
    return mask                   

def convert_to_text(month):
    lista1 = ['Ano Todo', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
             'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return lista1[month]