def conversao (a, b):
    if a.lower()=="quilômetros":
        res=b/1,60934
    elif a.lower()=="metros":
        res=medida*100
    elif a.lower()=="litros":
        res=medida*1000
    return res
un=input("Selecione a unidade entre quilômetros, metros e litros para a conversão: ")
medida=float(input("Diga a distância ou volume: "))
print(f"{conversao(un, medida)} é a medida convertida")