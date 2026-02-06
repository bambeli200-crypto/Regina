# Crear un programa que identifique los numeros primos.
n = int(input("Ingresa el número: "))

if n < 2:
    print("no es primo")
else:
    for k in range(2, n):
        if n % k == 0:
            print("no es primo")
            break
    else:
        print("es primo")
