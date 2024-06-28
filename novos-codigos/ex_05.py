# 5. Verificar se um Número Está em uma Lista
# Verifica se um número específico está presente em uma lista.

def esta_na_lista(numero, lista):
    return numero in lista

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]
numero_a_verificar = 30
presente = esta_na_lista(numero_a_verificar, numeros)
print(f"O número {numero_a_verificar} está na lista? {presente}")  # Output: O número 30 está na lista? True