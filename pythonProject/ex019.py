import random  # Importando o módulo random para sorteio aleatório

# Solicitar ao professor que insira o nome dos quatro alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Criar uma lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sortear um aluno aleatório da lista
aluno_escolhido = random.choice(alunos)

# Exibir o nome do aluno escolhido
print(f"O aluno escolhido para apagar o quadro foi: {aluno_escolhido}")