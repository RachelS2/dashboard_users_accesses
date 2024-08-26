import pandas as pd  

df = pd.read_json(r"C:\temp\Material\RachelS2\dashboard_users_accesses\random_data.json") 
df['date'] = pd.to_datetime(df['date'])

df['date'] = pd.to_datetime(df['date'])

# Função para determinar o turno
def get_shift(hour):
    if 0 <= hour < 6:
        return 'madrugada'
    elif 6 <= hour < 12:
        return 'manha'
    elif 12 <= hour < 18:
        return 'tarde'
    else:
        return 'noite'
    
def get_month(month):
    meses_do_ano = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses_do_ano[month - 1]

# Aplicando a função para criar a coluna 'shift'
df['shift'] = df['date'].dt.hour.apply(get_shift)

df['month'] = df['date'].dt.month.apply(get_month)

df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')

df.to_json(r"C:\temp\Material\Python para Data Science\exploring_fake_data\treated_data.json", orient='records', lines=True)
print("json gerado")