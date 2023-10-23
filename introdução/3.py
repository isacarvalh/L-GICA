n=int (input("Quantidade de notas?: "))

s=0

for c in range(1,n+1,1):
    notas= float (input("Informe a nota: "))
    s=s+notas
print (s/n)