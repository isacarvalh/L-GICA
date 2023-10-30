q_num= int(input("Informe a quantidade de números: "))

lista = []

s=0
m=1

for c in range (q_num):
    num= int(input("Informe o número: "))
    lista.append(num)
    s+=num
    m=m*num
print("A lista é: ", lista)
print("A soma é: ", s)
print("A multiplicação é: ",m)


