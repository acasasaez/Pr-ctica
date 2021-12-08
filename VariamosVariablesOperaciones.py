#Operaciones:
print ("Ejercicio 1: Operaciones numéricas")
dividendo = 7
divisor = 3
    #Si queremos obtener el resto de una dvisión empleamos el símbolo %. ej:
restoDivisión = dividendo % divisor
print (restoDivisión)
    #Si queremos obtener el conciente, entonces empleamos la barra
cociente = dividendo / divisor
print (cociente)
    #Sin embargo, si queremos el cociente como número entero ( como es en este caso donde la división no es exacta)
    #empleamos una doble barra:
cocienteEntero = dividendo // divisor
print (cocienteEntero)
    #Del mismo modo, si queremos multiplicar dos números emplearemos el asterisco
producto = dividendo * divisor
print (producto)
    #Por l contrario, si lo que queremos es conseguir el resultado de la potencia emplearemos un doble asterisco:
potencia = dividendo**divisor
print (potencia)
#Las operaciones, al igual que matemáticas, cuentan con un ordn de prevalecencia
# También podeos hacer operaciones con cadenas de caracteres
print ("Ejercicio 2: Operaciones con caracteres")
ejemplo1 = "mama" + "papa"
print (ejemplo1)
ejemplo2 = "mama"*5
print (ejemplo2)
#Como se puede ver, concatena

#Importante a tener en cuenta que las variables no son igualdades, sino asignaciones
# ```así, 
# si x = 3 
# x = x + 1 
# el valor final que tomará x es su valor más la unidad.

print ("Ejercicio 3: Cambio de variables")
#Ahora queremos crear un programa que intercambie el valor de 2 variables a y b
a = 3
b = 4
print ("el valor de a es", a)
print("el valor de b es",b)
#COmo es lógico, lo primero que se nos ocurriría es lo siguiente ´
# a = b
# b = a
# pero el error es lógico, si primero a toma el antiguo valor de b y luego b toma el valor de a2, entonces le estaremos asignando a a y b eñ mismo valor, el valor de b1.
# por lo tanto, la solución está en guardar el valor de a en una nueva variable (previamente), así:
a = 3
b = 4
print ("Valores iniciales")
print ("el valor de a es", a)
print("el valor de b es",b)
a2 = a
a = b
b = a2
print ("Valores tras el intercambio")
print ("el valor de a es", a)
print("el valor de b es",b)