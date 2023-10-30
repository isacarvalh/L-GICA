num_i = int (input("Informe o início: "))
num_f = int (input("Informe o final: "))

lista = []

for c in range(num_f,num_i-1,-1):
    lista.append(c)
print(lista)