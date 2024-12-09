import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt

# Função para gerar notas inteiras entre 0 e 10, com progressão crescente
def gerar_notas_crescentes():
    return [random.randint(0, 3), random.randint(3, 5), random.randint(5, 7), random.randint(7, 10)]

# Inicializando dados
materias = ["Português", "Matemática", "Ciências"]
bimestres = ["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"]

# Criando um DataFrame
data = []

for materia in materias:
    notas = gerar_notas_crescentes()
    for i, bimestre in enumerate(bimestres):
        data.append([materia, bimestre, notas[i]])

# Criar DataFrame
df = pd.DataFrame(data, columns=["Matéria", "Bimestre", "Nota"])

# Configurar o gráfico
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Criar o gráfico de linha
sns.lineplot(data=df, x="Bimestre", y="Nota", hue="Matéria", marker="o")

# Configurações adicionais do gráfico
plt.title("Evolução das Notas ao Longo dos Bimestres")
plt.xlabel("Bimestre")
plt.ylabel("Nota")
plt.legend(title='Matéria')
plt.ylim(0, 10)  # Ajusta o limite do eixo y para garantir que esteja entre 0 e 10

# Mostrar o gráfico
plt.show()

# Exportar para um arquivo CSV
output_file = "historico_notas_turma.csv"
df.to_csv(output_file, index=False)

# Mostrar o diretório atual e o caminho completo do arquivo exportado
import os
current_directory = os.getcwd()
full_path = os.path.join(current_directory, output_file)

print(f"Arquivo CSV gerado com sucesso!\nDiretório atual: {current_directory}\nCaminho completo do arquivo: {full_path}")
