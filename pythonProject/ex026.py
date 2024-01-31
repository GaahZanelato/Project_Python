# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Converte a frase para maiúsculas para facilitar a contagem
frase_maiuscula = frase.upper()

# Conta quantas vezes a letra "A" aparece
quantidade_a = frase_maiuscula.count("A")

# Encontra a posição da primeira ocorrência da letra "A"
posicao_primeira = frase_maiuscula.find("A") + 1  # Adiciona 1 para começar a contar a partir do 1, não do 0

# Encontra a posição da última ocorrência da letra "A"
posicao_ultima = frase_maiuscula.rfind("A") + 1  # Adiciona 1 para começar a contar a partir do 1, não do 0

# Exibe os resultados
print(f"\nA letra 'A' aparece {quantidade_a} vezes na frase.")
if quantidade_a > 0:
    print(f"A primeira ocorrência está na posição {posicao_primeira}.")
    print(f"A última ocorrência está na posição {posicao_ultima}.")
