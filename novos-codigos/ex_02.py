# 2. Cálculo da Média de Elementos em uma Lista
# Calcula a média dos elementos de uma lista de números.

def calcular_media(numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    return media

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"Média: {media}")  # Output: Média: 30.0