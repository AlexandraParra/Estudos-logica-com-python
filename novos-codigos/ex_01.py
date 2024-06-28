# 1. Soma de Elementos em uma Lista
# Calcula a soma de todos os elementos de uma lista de números.

def soma_lista(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(numeros)
print(f"Soma: {resultado}")  # Output: Soma: 15