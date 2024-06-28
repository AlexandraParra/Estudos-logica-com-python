# 6. Contagem de Vogais em uma String
# Problema: Escreva uma função que conte o número de vogais em uma string.

# Solução:

def contar_vogais(s):
    vogais = "aeiouAEIOU"
    return sum(1 for char in s if char in vogais)

# Teste
print(contar_vogais("Hello World"))  # Saída: 3