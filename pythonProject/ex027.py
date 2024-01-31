# Solicita ao usuário que digite o nome completo
nome_completo = input("Digite o nome completo: ")

# Separa o nome completo em partes usando o espaço como delimitador
partes_nome = nome_completo.split()

# Obtém o primeiro nome
primeiro_nome = partes_nome[0]

# Obtém o último nome
ultimo_nome = partes_nome[-1]

# Exibe os resultados
print(f"\nPrimeiro Nome: {primeiro_nome}")
print(f"Último Nome: {ultimo_nome}")
