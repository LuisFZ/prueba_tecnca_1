from decimal import Decimal
cadena = input("Ingresa un ISBN a validar: ")

isbn_trans = list(cadena.replace("-",""))


pos_isbn = 0
result = 0
resultados_mult = []

for i in [10,9,8,7,6,5,4,3,2,1]:
    oper = int(isbn_trans[pos_isbn])*int(i)
    resultados_mult.append(oper)
    pos_isbn += 1


for n in resultados_mult:
    result += n

evalua = Decimal(result%11)
if evalua == 0:
    print("Valido")
else:
    print("no valido")
