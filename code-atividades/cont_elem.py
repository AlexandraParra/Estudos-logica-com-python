# 10. Contagem de Elementos em uma Lista
# Problema: Escreva uma função que conte a ocorrência de cada elemento em uma lista.

# Solução:

def contar_elementos(lista):
    contagem = {}
    for elem in lista:
        if elem in contagem:
            contagem[elem] += 1
        else:
            contagem[elem] = 1
    return contagem

# Teste
print(contar_elementos([1, 2, 2, 3, 3, 3]))  # Saída: {1: 1, 2: 2, 3: 3}