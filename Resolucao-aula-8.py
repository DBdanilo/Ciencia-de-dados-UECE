import pandas as pd
import numpy as np

# Criação de 3 trumas com alunos ficticios
nomes_turma1 = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
                'Kleber', 'Laura', 'Marcelo', 'Natália', 'Otávio', 'Paula', 'Renato', 'Sabrina', 'Tadeu', 'Vera']
nomes_turma2 = ['Karla', 'Leonardo', 'Marina', 'Nicolas', 'Olivia', 'Pedro', 'Quintino', 'Rafaela', 'Sofia', 'Thiago',
                'André', 'Beatriz', 'Caio', 'Diana', 'Estevão', 'Fátima', 'Gustavo', 'Heloísa', 'Iara', 'João']
nomes_turma3 = ['Adriana', 'Bernardo', 'Clara', 'Diego', 'Eliana', 'Felipe', 'Giovana', 'Heitor', 'Ingrid', 'Jorge',
                'Karine', 'Luis', 'Marta', 'Natan', 'Otília', 'Patrícia', 'Ricardo', 'Simone', 'Tatiana', 'Vicente']

# geração aleatoria de notas para atribuição a cada aluno 
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

# Combinar os DataFrames das três turmas em um único DataFrame
df_combined = pd.concat([df_turma1, df_turma2, df_turma3], ignore_index=True)

print(df_combined)

