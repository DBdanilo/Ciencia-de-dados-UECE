import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Aluno Danilo Barbosa Macedo
#CIencias de Dados UECE
#Atividade 8

# Criação de 3 turmas com alunos fictícios
nomes_turma1 = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
                'Kleber', 'Laura', 'Marcelo', 'Natália', 'Otávio', 'Paula', 'Renato', 'Sabrina', 'Tadeu', 'Vera']
nomes_turma2 = ['Karla', 'Leonardo', 'Marina', 'Nicolas', 'Olivia', 'Pedro', 'Quintino', 'Rafaela', 'Sofia', 'Thiago',
                'André', 'Beatriz', 'Caio', 'Diana', 'Estevão', 'Fátima', 'Gustavo', 'Heloísa', 'Iara', 'João']
nomes_turma3 = ['Adriana', 'Bernardo', 'Clara', 'Diego', 'Eliana', 'Felipe', 'Giovana', 'Heitor', 'Ingrid', 'Jorge',
                'Karine', 'Luis', 'Marta', 'Natan', 'Otília', 'Patrícia', 'Ricardo', 'Simone', 'Tatiana', 'Vicente']

# Geração aleatória de notas para atribuição a cada aluno 
np.random.seed(42)  # Para reprodutibilidade
notas_turma1 = np.random.choice(['A', 'B', 'C'], len(nomes_turma1))
notas_turma2 = np.random.choice(['A', 'B', 'C'], len(nomes_turma2))
notas_turma3 = np.random.choice(['A', 'B', 'C'], len(nomes_turma3))

# Criar DataFrames separados para cada turma
df_turma1 = pd.DataFrame({
    'Nome': nomes_turma1,
    'Nota': notas_turma1,
    'Turma': 'Turma 1'
})

df_turma2 = pd.DataFrame({
    'Nome': nomes_turma2,
    'Nota': notas_turma2,
    'Turma': 'Turma 2'
})

df_turma3 = pd.DataFrame({
    'Nome': nomes_turma3,
    'Nota': notas_turma3,
    'Turma': 'Turma 3'
})

'''Código acima realiza a criação de cenário para desenvolvimento da atividade'''

'''Função para tratamento de notas em padrão numérico
Essa função resolve o item um da atividade'''
def transformar_notas(df):
    conversao_notas = {'A': 10, 'B': 8, 'C': 6}
    df['Nota'] = df['Nota'].map(conversao_notas)
    return df

df_turma1 = transformar_notas(df_turma1)
df_turma2 = transformar_notas(df_turma2)
df_turma3 = transformar_notas(df_turma3)



'''Função para resolução do item 2 da atividade realiza a validação para saber se as notas 
estão no intervalo entre 0 a 10, caso não esteja a nota inválida será substituída pela média geral
para não afetar as avaliações estatísticas

Na turma 01 Xavier foi colocado com nota de -4 para verificar a validação da nota e tratamento com troca 
pela média.
 
Na turma Yara foi colocado com nota 17 para o mesmo propósito.'''



def validar_e_substituir_notas(df):
    notas_validas = df['Nota'][(df['Nota'] >= 0) & (df['Nota'] <= 10)]
    media_notas = round(notas_validas.mean(), 2)
    df['Nota'] = df['Nota'].apply(lambda x: x if 0 <= x <= 10 else media_notas)
    return df

# Adicionando notas inválidas manualmente para testar
df_turma1.loc[df_turma1['Nome'] == 'Xavier', 'Nota'] = -4
df_turma2.loc[df_turma2['Nome'] == 'Yara', 'Nota'] = 17
# Supomos que df_combined já está criado e contém as colunas 'Nome', 'Nota' e 'Turma'

# Gráfico de dispersão das notas por turma
df_turma1 = validar_e_substituir_notas(df_turma1)
df_turma2 = validar_e_substituir_notas(df_turma2)
df_turma3 = validar_e_substituir_notas(df_turma3)

print("\nNotas após o tratamento de dados\nConcluindo a resolução do 1º e 2º item da atividade\n")
print("Turma 1:\n", df_turma1['Nota'])
print("Turma 2:\n", df_turma2['Nota'])
print("Turma 3:\n", df_turma3['Nota'])

'''resolução do item 3 junção dos data frames da tumas 1, 2 e 3 '''

df_combined = pd.concat([df_turma1, df_turma2, df_turma3], ignore_index=True)

print("\nDataFrame combinado:\n", df_combined)


'''utilização do matplt para geração de graficos para melhor visualização
resolução do item 4 da atividade'''

# Gráfico de distribuição das notas
plt.figure(figsize=(10, 6))
df_combined['Nota'].hist(bins=10, alpha=0.7)
plt.title('Distribuição das Notas')
plt.xlabel('Notas')
plt.ylabel('Frequência')
plt.grid(False)
plt.show()

# Gráfico de barras comparando a média de cada turma
media_turmas = df_combined.groupby('Turma')['Nota'].mean()
plt.figure(figsize=(10, 6))
media_turmas.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Média das Notas por Turma')
plt.xlabel('Turma')
plt.ylabel('Média das Notas')
plt.grid(False)
plt.show()


plt.figure(figsize=(10, 6))
for turma, cor in zip(['Turma 1', 'Turma 2', 'Turma 3'], ['blue', 'green', 'red']):
    subset = df_combined[df_combined['Turma'] == turma]
    plt.scatter(subset['Nome'], subset['Nota'], label=turma, color=cor, alpha=0.6)

plt.title('Dispersão das Notas por Turma')
plt.xlabel('Nome dos Alunos')
plt.ylabel('Notas')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()


