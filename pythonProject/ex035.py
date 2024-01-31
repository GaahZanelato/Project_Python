# Solicita o comprimento das três retas ao usuário
lado1 = float(input("Digite o comprimento da primeira reta: "))
lado2 = float(input("Digite o comprimento da segunda reta: "))
lado3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se os lados podem formar um triângulo
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
