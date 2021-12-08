#Hasta ahora todos nuestros programas realizan las mismas funciones.
#tomamos como referencia nuestro programam inicial que nos pedía nuesteo nombre y edad 
# si lo llevamos a un caso real sería interesante, por ejemplo, que nos diese diferentes resultados en funvión de la edad; para esto tenemos los condicionales.
#Un condicional consta de 3 partes:
    #La condición que queremos comprobar
    #La acción que se lleva a cabo si la condición se verifica
    #La acción que se lleva a cabo si la condición no se verifica 
#Retomamos nuestro antiguo programa:
print ("Ejercicio 1: Pedir y devolver datos")
print ("Cómo te llamas ?")
nombre = input()
print ("Cuál es tu año de nacimiento?")
year = int(input()) #los elementos que escribimos en el comando son interpretados coo cadenas de carcteres
#los int(), float()... nos permite transformarlos para que se almacenen como números enteros, decimales....
edad = 2021 - year
#print ("Hola", nombre, "tienes", edad, "años")
#ahora, vamos con el condicional, que se inicia con la palabra if:
if edad > 18:
    print ( "Hola", nombre, "eres muy viejo.")
#Recomendación: en estos casos, para comprobar que el código funciona conviene realizar varios intentos,
#a poder ser comprobando todas las condiciones para verificar que se cumple 
#en caso de que no se cumpla la condición, también podemos sugerir que el programa realice una acción
# esto se hace mediante un "else"
else:
    print ("Hola", nombre, "eres muy joven")

