# Solicita a velocidade do carro ao usuário
velocidade_carro = float(input("Informe a velocidade do carro em Km/h: "))

# Define o limite de velocidade
limite_velocidade = 80

# Verifica se o carro ultrapassou o limite de velocidade
if velocidade_carro > limite_velocidade:
    # Calcula a multa com base na velocidade acima do limite
    multa_por_km_excedido = 7.00
    km_excedidos = velocidade_carro - limite_velocidade
    valor_multa = km_excedidos * multa_por_km_excedido

    # Exibe a mensagem de multa
    print(f"Você foi multado! Velocidade excedida em {km_excedidos:.2f} Km/h.")
    print(f"Valor da multa: R${valor_multa:.2f}")
else:
    # Caso a velocidade esteja dentro do limite, exibe uma mensagem de que está dentro da velocidade permitida
    print("Você está dentro do limite de velocidade permitido. Dirija com segurança!")
