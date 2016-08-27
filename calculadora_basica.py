def suma(num,num2):
	operacion = int(num) + int(num2)

	print "el resultado es: " + str(operacion)

def resta(num,num2):
	operacion = int(num) - int(num2)

	print "el resultado es: " + str(operacion)

def divi(num,num2):
	operacion = float(num) / float(num2)

	print "el resultado es: " + str(operacion)

def multi(num,num2):
	operacion = int(num) * int(num2)

	print "el resultado es: " + str(operacion)




print "Calculadora Basica \n"

print "calculadora basica, ingresa un primer numero y luego ingresa el tipo de operacion + - * o / \n"
print "despues tu segundo numero "

uri = raw_input("ingresa primer numero Num1: ")

ope = raw_input("ingresa operacion + - / * : ")

num2 = raw_input("ingresa el segundo numero, Num2")


if (ope == "+") :
	suma(int(uri),int(ma))

elif(ope == "-") :
	resta(uri,num2)

elif(ope == "/") :
    divi(uri,num2)	

elif(ope == "*") :
	multi(uri,num2)

else :
	print "operacion invalida"
