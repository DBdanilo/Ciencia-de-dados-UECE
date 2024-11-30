import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados fornecidos
turma1 = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
             'Kleber', 'Laura', 'Marcelo', 'Natália', 'Otávio', 'Paula', 'Renato', 'Sabrina', 'Tadeu', 'Vera', 'Xavier'],
    'Nota': ['C', 'A', 'C', 'C', 'A', 'A', 'C', 'B', 'C', 'C', 'C', 'C', 'A', 'C', 'B', 'A', 'B', 'B', 'B', 'B', -4]
}

turma2 = {
    'Nome': ['Yara', 'Zeca', 'Alice', 'Beto', 'Cecília', 'David', 'Eva', 'Felix', 'Gisele', 'Karla', 'Leonardo', 'Marina',
             'Nicolas', 'Olivia', 'Pedro', 'Quintino', 'Rafaela', 'Sofia', 'Thiago', 'André'],
    'Nota': [17, 1, 7, 3, 1, 5, 5, 9, 3, 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'C', 'C', 'C', 'B']
}

turma3 = {
    'Nome': ['Beatriz', 'Caio', 'Diana', 'Estevão', 'Fátima', 'Gustavo', 'Heloísa', 'Iara', 'João', 'Hugo', 'Ivy', 'Jonas',
             'Katia', 'Lucas', 'Mila', 'Nino', 'Oscar', 'Paula', 'Quim', 'Adriana', 'Bernardo', 'Clara', 'Diego', 'Eliana',
             'Felipe', 'Giovana', 'Heitor', 'Ingrid', 'Jorge', 'Karine', 'Luis', 'Marta', 'Natan', 'Otília', 'Patrícia',
             'Ricardo', 'Simone', 'Tatiana', 'Vicente', 'Rita', 'Sandro', 'Tina', 'Ulisses', 'Violeta', 'William', 'Ximena',
             'Yuri', 'Zara', 'Afonso'],
    'Nota': ['C', 'B', 'B', 'C', 'B', 'C', 'C', 'A', 'C', 5, 1, 9, 1, 9, 3, 7, 6, 8, 7, 'A', 'C', 'C', 'A', 'A', 'C', 'B',
             'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 4, 1, 4, 7, 9, 8, 8, 0, 8, 6, 8, 7]
}



''' Função para tratamento de notas em padrao numerico
Essa função revolve o item um da atividade'''
def transformar_notas(data):
    conversao_notas = {'A': 10, 'B': 8, 'C': 6}
    data['Nota'] = [conversao_notas.get(nota, nota) for nota in data['Nota']]
    return data
turma1 = transformar_notas(data=turma1)
turma2 = transformar_notas(data=turma2)
turma3 = transformar_notas(data=turma3)

'''Função para resolução do item 2 da atividade realiza a validação para saber se as notas 
estão no intervalo entre 0 a 10, caso não esteja a nota invalida sera subistituida pela media geral
para não afetar as avaliações estatisticas

 Na turma 01 Xavier foi colocado com nota de -4 para verificar a validação da nota e tratamento com troca 
 pela media.
 
 na turma Yara foi colocado com nota 17 para o mesmo proposito.

'''
def validar_e_substituir_notas(data):
    notas = data['Nota']
    notas_validas = [nota for nota in notas if 0 <= nota <= 10]
    if len(notas_validas) == 0:
        media_notas = 0
    else:
        media_notas = sum(notas_validas) / len(notas_validas)
        media_notas = round(media_notas, 2)

    data['Nota'] = [nota if 0 <= nota <= 10 else media_notas for nota in notas]
    return data
turma1 = validar_e_substituir_notas(turma1)
turma2 = validar_e_substituir_notas(turma2)
turma3 = validar_e_substituir_notas(turma3)


print("\n notas após o tratamento de dados\n Concluindo a resolução do 1º e 2º item da atividade\n",turma1['Nota'],turma2['Nota'], turma3['Nota'])


#geração dos data frames das 3 turmas 
df1 = pd.DataFrame(turma1)
df2 = pd.DataFrame(turma2)
df3 = pd.DataFrame(turma3)

print(df1)
print(df2)



