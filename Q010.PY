numero = int(input("digite um numero:"))
print(f"tabuada de {numero}:")
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")