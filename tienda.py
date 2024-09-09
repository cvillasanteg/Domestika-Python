print("******************************")
print("****     Bienvenidos a    ****")
print("*** la tienda de mascostas ***")
print("******************************")

numPerros = 10
numGatos = 8
numPajaros = 25
animalesTotales = numPerros + numGatos + numPajaros

print("Porfavor escribe tu nombre:")
nombre = input()
print("Porfavor escribe tu apellido:")
apellido = input()
nombreCompleto = nombre + " " + apellido

print("Gracias por visitarnos", nombreCompleto)

print("Perros:",numPerros)
print("Gatos:",numGatos)
print("Pajaros:",numPajaros)
print("Actualmente contamos con: ", animalesTotales,"animales")