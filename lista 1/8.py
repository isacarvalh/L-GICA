q_notas = int(input("Quatidade de notas: "))

lista = []
s=0

for c in range(q_notas):
    notas=float(input("Digite a nota: "))
    lista.append(notas)
    s+=notas

print("Notas: ", lista)
print("Média: ", s/q_notas)
