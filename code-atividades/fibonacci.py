# 3. Sequência de Fibonacci
# Problema: Escreva uma função que retorne a sequência de Fibonacci até o n-ésimo termo.

# Solução:

def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

# Teste
print(fibonacci(10))  # Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]