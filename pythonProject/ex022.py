nome_completo = input("Digite seu nome completo: ")

# Transforma o nome para maiúsculas
nome_maiusculo = nome_completo.upper()

# Transforma o nome para minúsculas
nome_minusculo = nome_completo.lower()

# Remove os espaços e conta o total de letras
total_letras = len(nome_completo.replace(" ", ""))

# Encontra o primeiro nome e conta o total de letras
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)

# Exibe os resultados
print(f"\nNome em maiúsculas: {nome_maiusculo}")
print(f"Nome em minúsculas: {nome_minusculo}")
print(f"Total de letras (sem considerar espaços): {total_letras}")
print(f"Total de letras no primeiro nome: {letras_primeiro_nome}")
