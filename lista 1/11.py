nome= input("Informe o nome do atleta: ")

lista = []
s=0

for c in range(1,6):
    salto= float(input("Informe o salto: "))
    lista.append(salto)
    s+=salto
m=s/5
print("Atleta: ", nome)
print("Saltos: ", lista)
print("A média dos saltos: ", m)