# 4. Concatenar Strings em uma Lista
# Concatena todas as strings em uma lista em uma única string.

def concatenar_strings(lista_de_strings):
    resultado = ""
    for string in lista_de_strings:
        resultado += string
    return resultado

# Exemplo de uso
palavras = ["Olá, ", "mundo", "!"]
texto_concatenado = concatenar_strings(palavras)
print(f"Texto concatenado: {texto_concatenado}")  # Output: Texto concatenado: Olá, mundo!