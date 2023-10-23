p=0
i=0

for cont in range (0,10):
    num= int(input("INFORME UM NÚMERO:"))
    if num%2 == 0:
        p+=1
    else:
        i+=1
print(f"PARES: {p}")
print(f"ÍMPARES: {i}")
