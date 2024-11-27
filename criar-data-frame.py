import pandas as pd
import numpy as np

# Nomes fictícios de alunos para cada turma
nomes_turma1 = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
                'Kleber', 'Laura', 'Marcelo', 'Natália', 'Otávio', 'Paula', 'Renato', 'Sabrina', 'Tadeu', 'Vera']
nomes_turma2 = ['Karla', 'Leonardo', 'Marina', 'Nicolas', 'Olivia', 'Pedro', 'Quintino', 'Rafaela', 'Sofia', 'Thiago',
                'André', 'Beatriz', 'Caio', 'Diana', 'Estevão', 'Fátima', 'Gustavo', 'Heloísa', 'Iara', 'João']
nomes_turma3 = ['Adriana', 'Bernardo', 'Clara', 'Diego', 'Eliana', 'Felipe', 'Giovana', 'Heitor', 'Ingrid', 'Jorge',
                'Karine', 'Luis', 'Marta', 'Natan', 'Otília', 'Patrícia', 'Ricardo', 'Simone', 'Tatiana', 'Vicente']

# Novos nomes fictícios
novos_nomes_turma1 = ['Xavier', 'Yara', 'Zeca', 'Alice', 'Beto', 'Cecília', 'David', 'Eva', 'Felix', 'Gisele']
novos_nomes_turma2 = ['Hugo', 'Ivy', 'Jonas', 'Katia', 'Lucas', 'Mila', 'Nino', 'Oscar', 'Paula', 'Quim']
novos_nomes_turma3 = ['Rita', 'Sandro', 'Tina', 'Ulisses', 'Violeta', 'William', 'Ximena', 'Yuri', 'Zara', 'Afonso']

# Gerar notas aleatórias para as três turmas
np.random.seed(42)  # Para reprodutibilidade
notas_turma1_letras = np.random.choice(['A', 'B', 'C'], 20)
notas_turma2_letras = np.random.choice(['A', 'B', 'C'], 20)
notas_turma3_letras = np.random.choice(['A', 'B', 'C'], 20)

# Gerar notas aleatórias entre 0 e 10
notas_turma1_numericas = np.random.randint(0, 11, 10)
notas_turma2_numericas = np.random.randint(0, 11, 10)
notas_turma3_numericas = np.random.randint(0, 11, 10)

# Combinar nomes e notas
nomes_turma1.extend(novos_nomes_turma1)
nomes_turma2.extend(novos_nomes_turma2)
nomes_turma3.extend(novos_nomes_turma3)

notas_turma1 = np.concatenate((notas_turma1_letras, notas_turma1_numericas), axis=None)
notas_turma2 = np.concatenate((notas_turma2_letras, notas_turma2_numericas), axis=None)
notas_turma3 = np.concatenate((notas_turma3_letras, notas_turma3_numericas), axis=None)

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
