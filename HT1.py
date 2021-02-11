print("Ingrese un número")
numero=int(input(""))
i=1
for i in range(numero):
   print("*"*(i+1))

print("")
print("Ingrese un número")
numerodos=int(input(""))
contador=0
j=1
while j<=numerodos:
    if numerodos%j==0:
        contador=contador+1
    j=j+1
if contador==2:
    print("El numero es primo")
if contador!=2:
    print("El numero no es primo")