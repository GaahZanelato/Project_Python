# Solicitar ao usuário que insira a quantidade de Km percorridos e a quantidade de dias de aluguel
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

# Definir as taxas de custo
custo_diario = 60  # R$60 por dia
custo_por_km = 0.15  # R$0,15 por Km

# Calcular o preço total a pagar
preco_a_pagar = (dias_aluguel * custo_diario) + (km_percorridos * custo_por_km)

# Exibir o resultado
print(f"O preço a pagar pelo aluguel do carro é de R${preco_a_pagar:.2f}.")