# 1. Cálculo de Fatorial
# Problema: Escreva uma função que calcule o fatorial de um número n.

# Solução:

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Teste
print(fatorial(5))  # Saída: 120