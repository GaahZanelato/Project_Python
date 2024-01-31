import random

def jogo_adivinhacao():
    # Escolhe um número aleatório entre 0 e 5
    numero_pensado = random.randint(0, 5)

    # Pede para o usuário tentar adivinhar o número
    tentativa = int(input("Tente adivinhar o número pensado pelo computador (entre 0 e 5): "))

    # Verifica se a tentativa do usuário está correta
    if tentativa == numero_pensado:
        print(f"Parabéns! Você acertou. O número pensado foi {numero_pensado}.")
    else:
        print(f"Você errou. O número pensado foi {numero_pensado}.")

# Chama a função para iniciar o jogo
jogo_adivinhacao()
