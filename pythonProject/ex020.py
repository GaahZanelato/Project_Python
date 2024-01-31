import random  # Importando o módulo random para sorteio aleatório

# Solicitar ao professor que insira o nome dos quatro alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Criar uma lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralhar a ordem da lista
random.shuffle(alunos)

# Exibir a ordem sorteada
print("A ordem de apresentação dos trabalhos é:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")