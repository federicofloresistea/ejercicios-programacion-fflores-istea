#pongo bariables que clras y que no especificquen un numero( porque poner de nombre a la variable "numero2" podria entenderse como que el input a poner es el "2") 
primer_numero = input("ingrese el primer numero : ")
segundo_numero = input("ingrese el segundo numero : ")
#convierto el resultado de la variable a dato entero para poder hacer las operaciones
print("la suma de los numeros es: ", int(primer_numero) + int(segundo_numero)) 
#especifico que variable es el minuendo y cual es esl sutrendo   
print("la resta delprimer numero menos el sgundo numero es: ", int(primer_numero) - int(segundo_numero))
print("la resta del sgundo numero menos el primer numero es: ", int(segundo_numero) - int(primer_numero))
#especifico cual es el dividendo y cual es el divisor
print("la division del primer numero entre el segundo numero es: ", int(primer_numero) / int(segundo_numero))
print("la division del segundo numero entre el primer numero es: ", int(segundo_numero) / int(primer_numero))
#no hace falta especificar el orden de la multiplicacion porque el resultado es el mismo
print("la multiplicacion de los numeros es: ", int(primer_numero) * int(segundo_numero))