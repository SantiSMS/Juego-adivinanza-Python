import random

numero_secreto = random.randint(0,100)
cantidad_intentos = 0
cantidad_max = 5

adivinado = False

print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado and cantidad_intentos < cantidad_max:
    entrada = input("Introduce un numero del 0 al 99: ")
    numero = int(entrada)
    
    if numero == numero_secreto:
        print("has adivinado")
        adivinado = True
    elif numero < numero_secreto:
        print("Numero mayor")
    else: 
        print("numero menor")
    cantidad_intentos += 1

if not cantidad_intentos < cantidad_max: 
    print ("game over")

