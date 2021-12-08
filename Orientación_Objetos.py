#A continuación intentaremos entender de que va la programación orientada a objetos.
#Diferenciamos: (Metáfora)
    #El objeto genérico: Coche (puede ser cualquiera)
    #La instancia: Mi coche (es un objeto concreto)
    #Los atributos: Mercedes, Rojo, familiar... (características de nuestro objeto concreto)
    #Los métodos: arrancar, frenar, acelerar, aparcar.... (las acciones que puede llevar a cabo)
# En programación pasa algo similar:
#un ejemplo son las listas, un objeto genérico, pero nuestra lista será una instancia
#así, esta cuenta con una características, como su longitud
#del mismo modo, tenemos que sobre esta se pueden llevar a cabo x funciones, por ejemplo, agregarun nuevo elemento
# Es importante diferenciar los atributos de las instancias, pues estas últimas son funciones. Continuando con el ejemplo del coche:
   #mi_coche.color = rojo, es un atributo
   # sin embargo, mi_coche.arrancar()
   # lista.remove: elimina un valor
   #lista.pop(): elimina el valor final y lo devuelve
   #lista.append("h"): agrega un valor al final
   # lista.extend(["i", "j"]): agrega una lista al final
    #lista.insert(2, "d") : nos permite agregar valores en cualquier posición
print ("Jugando con listas")
nombres = ["Juan","Pedro","Martín","Rubén"]
while not "Manolo" in nombres:
    nombres.insert(0, "Manolo")
print (nombres)
while "Martín" in nombres:
    nombres.remove("Martín")
    print (nombres)
#Para emplear los métodos en listas es necesario utilizar el while while not, ya que estas son mutables.