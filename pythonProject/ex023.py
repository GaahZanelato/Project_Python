# Solicita ao usuário que digite um número de 0 a 9999
numero = int(input("Digite um número de 0 a 9999: "))

# Obtém cada dígito separadamente
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Exibe os resultados
print(f"\nUnidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
