# Solicita ao usuário que digite o nome
nome = input("Digite o nome completo: ")

# Verifica se o nome contém "SILVA" (ignorando maiúsculas/minúsculas)
contem_silva = "SILVA" in nome.upper()

# Exibe o resultado
if contem_silva:
    print(f"\nO nome {nome} contém 'SILVA'.")
else:
    print(f"\nO nome {nome} não contém 'SILVA'.")
