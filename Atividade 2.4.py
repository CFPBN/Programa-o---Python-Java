def media (a, b, c):
    ma=((a+b+c)/3)
    if ma>=7:
        return "Aprovado"
    else:
        return "Reprovado"
n1=float(input("Informe a primeira nota: "))
n2=float(input("Informe a segunda nota: "))
n3=float(input("Informe a terceira nota: "))
print(media(n1, n2, n3))