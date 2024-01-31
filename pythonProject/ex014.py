# Solicitar ao usuário que insira a temperatura em Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Calcular a temperatura em Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Exibir o resultado
print(f"{temperatura_celsius} graus Celsius é igual a {temperatura_fahrenheit:.2f} graus Fahrenheit.")