# Solicita o salário do funcionário ao usuário
salario = float(input("Digite o salário do funcionário: R$"))

# Verifica o valor do aumento com base no salário
if salario > 1250.00:
    aumento_percentual = 10
else:
    aumento_percentual = 15

# Calcula o valor do aumento
aumento = (salario * aumento_percentual) / 100

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe o resultado na tela
print(f"Salário antes do aumento: R${salario:.2f}")
print(f"Percentual de aumento: {aumento_percentual}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
