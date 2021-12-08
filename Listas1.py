#Una vez conocidas las variables pasamos a estudiar otros tipos de almacenamiento de datos, como las listas:
#Características de las listas:
    #Están ordenadas, tienen un elemento primero, segundo... que la máquina los ordena como el elemento 0,1,2...
    #Pueden estar compuestas por todo tipo de caracteres
    #Igual que las variables están nombradas
print("Probando con listas")
lista = [2, "Juan", 8.9]
print (lista) 
print (lista[0]) #podemos llamar a elementeos determinados de la lista
print (lista[2])
#Lista de listas:
#También es posible elaborar una lista ue esté compuesta por otras listas:
#ejemplo:
print ("Lista de listas")
mi_aula =[["Juan", "Pedro", "Marta", "Julia"], ["Arturo", "Cecilia"], ["Lorena", "Emilia", "Roberta"]]
print ("Equipo 1:", mi_aula[0])
print ("Equipo 2:", mi_aula[1])
print ("Equipo 3:", mi_aula[2])
#Ya habíamos estudiados algunas funciones como print(), input(), int()...
#estudiemos ahora una función muy util con listas, que es len()
print("probando la función len()")
equipos = len(mi_aula)
print ("número de equipos", equipos)
e1 = len (mi_aula[0])
e2 = len(mi_aula[1])
e3 = len(mi_aula [2])
print ("número de participantes")
print ("equipo 1:", e1)
print("equipo 2:", e2)
print ("equipo 3:", e3)
#Como puedes observar, esta función nos devuelve el número de elementos que hay en cada lista
#Tanto el índice, como la función len() nos serán muy útiles para movernos dentro de listas, 
#sin embargo, existen otras opraciones que podemos realizar dentro de las mismas,por ejemplo, unir y separar listas.
#ejemplo:
print("Unir listas")
perdedores = mi_aula[0] + mi_aula [2]
print ("Los alumnos que no han recibido ningún premio son:", perdedores)
print("DE OTRA MANERA")#así ahorramos líneas de código innecesarias
print ("Los alumnos que no han recibido ningún premio son:",mi_aula[0] + mi_aula [2] )
print("separar listas")
ganadores = mi_aula[:1]
perdedores = mi_aula [1:]
tercera_posición = mi_aula[2:]
print ("El equipo ganador es:", ganadores)
print ("Los equipos perdedores son;", perdedores)
print ("El equipo en tercera posición es:",tercera_posición)
print("DE OTRA MANERA")#así ahorramos líneas de código innecesarias
print ("El equipo ganador es:", mi_aula[:1])
print ("Los equipos perdedores son;", mi_aula [1:])
print ("El equipo en tercera posición es:",mi_aula [2:])
#También podemos sobre escribir elementos 
print ("Cambiamos el quipo 2")
mi_aula[1]= ["Manola", "Pedro"]
print (mi_aula)
#También existe la opción delete - eliminar elemento
print ("ELIMINAMOS SEGUNDO EQUIPO")
del mi_aula[2]
print (mi_aula)
print ("EJERCICIO DNI")
#Para asignar tu letra del dni se toma el número, se divide entre 23 y se toma el resto.
#La letra que coincide con el número de este resto equivale a tu letra del dni.
tu_letra = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print ("Introduce tu DNI sin letra")
tu_dni = int(input())
val = tu_dni % 23
print ("La letra de tu dni es:", tu_letra[val])
