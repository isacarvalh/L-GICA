n=int(input("Quantas provas?; "))

s=0

for c in range(n):
    v=float(input("Nota: "))
    s=s+v
m=s/n
print(f"MÉDIA: {m:.2f}")