# Solicita três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Encontra o maior e o menor entre os três números
maior_numero = max(numero1, numero2, numero3)
menor_numero = min(numero1, numero2, numero3)

# Exibe o resultado na tela
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
