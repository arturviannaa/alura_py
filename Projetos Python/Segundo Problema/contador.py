# Código inicial

# frase = input("Digite uma frase: ")
# palavras = frase.split()
# print(len(palavras))
# print(palavras)

def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ",.!|?;:\"'()[]{}"

    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras(frase):
    frase = limpar_texto(frase)

    if not frase.strip():
        return {}

    palavras = frase.split()
    contagem = {}

    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem