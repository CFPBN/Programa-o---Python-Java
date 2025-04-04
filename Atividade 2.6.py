def contador (a):
    n=0
    vogais="aeiou"
    for i in a:
        if i.lower() in vogais:
            n+=1
    return n
frase=input("Escreva uma palavra ou frase para contar suas vogais: ")
print(contador(frase))