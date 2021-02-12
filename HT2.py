#ejercicio 1
con="contraseña"
print("Escriba una su contraseña")
contra=input().lower()
if con==contra:
    print("Su contraseña es correcta")
if con!=contra:
    print("Su contraseña es incorrecta")

#ejercicio 2
print("Ingrese su nombre")
var1=input().lower()
print("Ingrese su sexo (Hombre o Mujer)")
var2=input().lower()
if var2=="mujer":
    if var1<"m":
        print("Su grupo es el A")
    else:
        print("Su grupo es el B")
if var2=="hombre":
    if var1>"n":
        print("Su grupo es el A")
    else:
        print("Su grupo es el B")
