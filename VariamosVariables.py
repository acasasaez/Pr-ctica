#Sabemos pedir datos y devolverlos, pero aun no hemos hecho nada con ellos 
#Creemos un progrma que pida el nombre y el año de nacimieto y
 #devuelva "Hola, nombre, tines edad años
print ("Ejercicio 1: Pedir y devolver datos")
print ("Cómo te llamas ?")
nombre = input()
print ("Cuál es tu año de nacimiento?")
year = int(input()) #los elementos que escribimos en el comando son interpretados coo cadenas de carcteres
#los int(), float()... nos permite transformarlos para que se almacenen como números enteros, decimales....
edad = 2021 - year
print ("Hola", nombre, "tienes", edad, "años")
#anotación, ponemos el input directamente dentro de la variable que nos sale, como se puede observar.
#```si ponemos esas tres comillas, se interpreta que el comentario va a ocupar más de una linea
# y así, cuando cambiamos de linea
# ni hace falta volver a poner la almohadilla, justo como estamos
# comprobando ahora`

