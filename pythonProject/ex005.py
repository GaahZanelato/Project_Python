# Passo 1: Entrada de dados
numero = input("Digite um número inteiro: ")

# Passo 2: Conversão para inteiro
numero_inteiro = int(numero)

# Passo 3: Cálculo do sucessor e antecessor
sucessor = numero_inteiro + 1
antecessor = numero_inteiro - 1

# Passo 4: Exibição dos resultados
print(f"O sucessor de {numero_inteiro} é {sucessor}.")
print(f"O antecessor de {numero_inteiro} é {antecessor}.")