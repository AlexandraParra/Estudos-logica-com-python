# 7. Verificação de Palíndromo
# Problema: Escreva uma função para verificar se uma palavra é um palíndromo.

# Solução:

def eh_palindromo(s):
    return s == s[::-1]

# Teste
print(eh_palindromo("radar"))  # Saída: True
print(eh_palindromo("python")) # Saída: False