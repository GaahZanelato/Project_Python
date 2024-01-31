# Solicita a distância da viagem ao usuário
distancia_viagem = float(input("Digite a distância da viagem em Km: "))

# Define as taxas por Km
taxa_curta = 0.50  # para viagens de até 200 Km
taxa_longa = 0.45  # para viagens mais longas

# Calcula o preço da passagem com base na distância
if distancia_viagem <= 200:
    preco_passagem = distancia_viagem * taxa_curta
else:
    preco_passagem = distancia_viagem * taxa_longa

# Exibe o preço da passagem
print(f"O preço da passagem para uma viagem de {distancia_viagem} Km é R${preco_passagem:.2f}.")
