# Solicita ao usuário que digite o nome da cidade
nome_cidade = input("Digite o nome da cidade: ")

# Verifica se o nome da cidade começa com "SANTO" (ignorando maiúsculas/minúsculas)
comeca_com_santo = nome_cidade.upper().startswith("SANTO")

# Exibe o resultado
if comeca_com_santo:
    print(f"\nO nome da cidade {nome_cidade} começa com 'SANTO'.")
else:
    print(f"\nO nome da cidade {nome_cidade} não começa com 'SANTO'.")
