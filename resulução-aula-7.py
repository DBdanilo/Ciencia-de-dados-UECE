import pandas as pd
import numpy as np

# Dados de entrada
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [28, 34, 29, None, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', None, 'Curitiba', 'Belo Horizonte'],
    'Vendas': [150, 200, 300, 400, None]
}

# 1. Criar o DataFrame
df = pd.DataFrame(dados)
print("DataFrame Original:")
print(df)

# 2. Filtrar os clientes que têm mais de 30 anos
filtro_mais_30 = df[df['Idade'] > 30]
print("\nClientes com mais de 30 anos:")
print(filtro_mais_30)

# 3. Calcular a média de idade dos clientes
media_idade = df['Idade'].mean()
print("\nMédia de idade dos clientes:")
print(media_idade)

# 4. Substituir valores faltantes na coluna Cidade por ‘Desconhecido’
df['Cidade'] = df['Cidade'].fillna('Desconhecido')
print("\nDataFrame após substituir valores faltantes na coluna Cidade:")
print(df)

# 5. Calcular a soma total das vendas
soma_vendas = df['Vendas'].sum()
print("\nSoma total das vendas:")
print(soma_vendas)
