#muy bien, una vez entendidos los condicionales, pasemos a estudiar condicionales anidados
#o dicho de otra manera, condicionales dentro de otros condicionales.
# ejemplo:
#En ua fiesta el número de invitados no puede ser superior a 10 ni iferior a 5, elabora un programa que te indique si la fiesta se puede realizar o no ( conforme al número de invitados)
print ( "EJERCCICIO 1")
print ("Cuántos invitados son ?")
invitados = int(input())
if invitados > 5:
    if invitados > 10:
        print ("No hay fiesta")
    else:
        print ("Hay fiesta")
else:
    print ("No hay fiesta")

#A veces podemos abreviar estos condicionales con un elif (else...if), sabiendo que no se cumple la primera condición, se cumple la segunda?
print ("EJERCICIO 1: MEJORADO")
print ("Cuántos invitados son ?")
invitados = int(input())
if invitados > 10:
    print ("No hay fiesta")
elif invitados > 5:
    print ("Hay fiesta")
else:
    print ("No hay fiesta")

print ("EJERCICIO 2.")
#El lector tiene que adivinar un número del 1 al 3, siendo 2 el resultado:
test = int(input())
if test == 1 or test == 3:
    print ("No ha acertado")
elif test == 2:
    print ("Has acertado")
else:
    print ("No has escrito un número entre el 1 y el 3")
#En este caso es sencillo porque las opciones son excluyentes, pero en otros casos
#hay que ser cuidadoso para escoger adecuadamente las condiciones y en el orden
#que se piden, quién se anida en quién...y, finalmente, hacer pruebas para todos los
#casos posibles.
#Esto podría usarse para crear un “menú”.