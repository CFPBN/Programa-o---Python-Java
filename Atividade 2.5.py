def tabuada (a):
    lista=[]
    for i in range (1,11):
        lista.append(a*i)
    return lista
n=int(input("Digite o número para ver sua tabuada: "))
print(*tabuada (n), sep=", ")