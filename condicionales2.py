# vamos con un caso más complejo, imaginemos que en una atracción solo pueden subir niños mayores de 10 años o que midan más de un metro
print ("Ejercicio 3; Modifiación del anterior")
#entonces introduciomos una nueva variable:
print ("Cómo te llamas ?")
nombre = input()
print ("Cuál es tu año de nacimiento?")
year = int(input()) #los elementos que escribimos en el comando son interpretados coo cadenas de carcteres
#los int(), float()... nos permite transformarlos para que se almacenen como números enteros, decimales....
edad = 2021 - year
print ("Cuánto mides?")
altura = float (input())
#ahora creamos nuestro condicional con un "or", que indica que la accioón se ejecuta si se da al menos una de las 2 condiciones:
if edad >= 10 or altura >= 1.0 :
    print ("Puede subir en la atracción")
else:
    print ("No puede subir en la atracción")
# del mismo modo que hemos empleado el or, también podemos utilizar el "and" y el "not":
#también es necesario recordar lo siguiente
    #es posible hacer comparaciones, pero el signo = sirve para asignar valores, por lo tannto si la condición que queremos omparar 
    # es, por ejemplo, que a sea igual a 18, deberemos escribir : a == 18
    #por otro lado, también podemos usar las siguientes condiciones: mayor o igual (>=), menor o igual (<=), distinto (!=)
     