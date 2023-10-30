q_num= int(input("Informe a quantidade de números: "))

lista = []

par = []
impar = []

for c in range(q_num):
    num= int(input("Informe o número: "))
    lista.append(num)
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
print("Números Informados: ", lista)
print("Números Pares: ", par)
print("Números Impares: ", impar)

