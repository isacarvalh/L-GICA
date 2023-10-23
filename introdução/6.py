t= int(input("Montar a tabuada de "))
b= int(input("Começar por "))
e= int(input("Acabar em "))

for c in range(b,e+1):
    print(f"{t} x {c} = {t*c}")