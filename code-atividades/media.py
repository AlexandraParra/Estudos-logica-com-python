# 8. Cálculo da Média de uma Lista
# Problema: Escreva uma função que calcule a média dos elementos de uma lista.

# Solução:

def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0

# Teste
print(media_lista([1, 2, 3, 4]))  # Saída: 2.5