# 3. Encontrar o Maior Elemento em uma Lista
# Encontra e retorna o maior número em uma lista.

def encontrar_maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

# Exemplo de uso
numeros = [10, 25, 30, 5, 15]
maior_numero = encontrar_maior(numeros)
print(f"Maior número: {maior_numero}")  # Output: Maior número: 30