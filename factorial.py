numero = input("Ingresa el número a calcular factorial: ")
total = int(numero)
digito = int(numero)

for i in range(int(numero)):
    digito -= 1
    if digito != 0:
        total = total * digito
        print(total)
    

