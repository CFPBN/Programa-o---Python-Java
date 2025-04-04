def operacoes (a, b, c):
    if c=="+":
        res=a+b
    elif c=="-":
        res=a-b
    elif c=="*":
        res=a*b
    elif c=="/":
        res=a/b
    return res
n1=float(input("Selecione o primeiro número: "))
n2=float(input("Selecione o segundo número: "))
op=input("Selecione a operação entre +, -, * e /: ")
print(operacoes(n1, n2, op))