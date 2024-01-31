import math  # Importando o módulo math para usar funções trigonométricas

# Passo 1: Entrada de Dados
angulo_graus = float(input("Digite o valor do ângulo em graus: "))

# Passo 2: Conversão para Radianos
angulo_radianos = math.radians(angulo_graus)

# Passo 3: Cálculo do Seno, Cosseno e Tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Passo 4: Exibição dos Resultados
print(f"Para o ângulo {angulo_graus} graus:")
print(f"O seno é {seno:.4f}")
print(f"O cosseno é {cosseno:.4f}")
print(f"A tangente é {tangente:.4f}")