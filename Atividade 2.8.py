def teste (a):
    if a.lower()==a.lower()[::-1]:
        return "A palavra é um palíndromo"
    else:
        return "A palavra não é um palíndromo"
x=input("Diga a palavra para verificar se é um palíndromo: ")
print (teste(x))