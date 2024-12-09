import pandas as pd
import random

# Função para gerar notas aleatórias entre 0 e 10
def gerar_nota():
    return round(random.uniform(0, 10), 2)

# Inicializando dados
materias = ["Português", "Matemática", "Ciências"]
alunos = [f"Aluno {i+1}" for i in range(10)]
bimestres = ["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"]

# Criando um DataFrame
data = []

for aluno in alunos:
    for materia in materias:
        for bimestre in bimestres:
            data.append([aluno, materia, bimestre, gerar_nota()])

# Criar DataFrame
df = pd.DataFrame(data, columns=["Aluno", "Matéria", "Bimestre", "Nota"])

# Exportar para um arquivo CSV
df.to_csv("notas_ficticias.csv", index=False)

print("Arquivo CSV gerado com sucesso!")
