print "Secuencia de fibonacci \n"
print "Indica asta donde quieres que llegue la secuencia"

secuencia = raw_input("numero de iteraciones")

operacion = 0
num = 1

for x in range(0,int(secuencia)) :

	resultado = operacion + num
	print resultado

	operacion = num
	num = resultado
