# 2. Verificação de Número Primo
# Problema: Escreva uma função para verificar se um número é primo.

# Solução:
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Teste
print(eh_primo(11))  # Saída: True
print(eh_primo(4))   # Saída: False