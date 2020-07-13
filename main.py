import random 
numerodeintentos = 0
numerominimo = 0
numeromaximo = 100

print("Hola! como es tu nombre?: ")
nombredeusuario = input()

numero = random.randint(numerominimo, numeromaximo)
print("Bien, " + nombredeusuario + ". Estoy pensando en un numero entre " + str(numerominimo) + " y " + str(numeromaximo))

#Se encarga de ejecutar nuestro juego#
while numerodeintentos < 6:
    print("Adivina el numero, tienes 6 intentos: ")
    guess = input()
    guess = int(guess)

    numerodeintentos = numerodeintentos + 1

    if guess < numero:
        print("Tu numero es demasiado bajo.")
    if guess > numero:
        print("Tu numero es demasiado alto.")
    if guess == numero:
        break
if guess == numero:
    numerodeintentos = str(numerodeintentos)
    print("Has adivinado " + nombredeusuario + "! has acertado en " + numerodeintentos + " intentos")
else:
    numerodeintentos > 6
    numero = str(numero)
    print("Perdiste, el numero era " + numero)
