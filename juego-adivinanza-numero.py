#RESUMIR TODO DENTRO DE UNA FUNCION Y DSP EJECUTAR
#todo lo q pase va a estar dentro del juego. va a ser programacion funcional porq va a ser todo dentro de una funcion.

import random


def juego_adivinanza():
    #Generar un numero del 1 al 100 y atraves de un input ir adivinando
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False #(falso hasta q se haga positiva)

    #Primeras lineas del juego donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de numero!")
    print("Debes adivinar un numero entre 1 al 100")
    print("Intenta adivinar")

    #Bucle:
    
    while not adivinado:
        # solicitar un numero
        adivinanza= input("Introduzca un numero del 1 al 100: ") #INPUT para pedirle a la persona. esto es un STRING

        # verificar que la entrada sea un numero
        if adivinanza.isdigit(): #esto para confirmar que nos manden un DIGITO
            adivinanza= int(adivinanza) #aca para cambiar de STRING(texto)(q es el int(adivinanza) a NUMBER(entero) que es adivinanza=)
            intentos += 1 

            if adivinanza < numero_secreto:                               #SI ESTE NUMERO ESTE NUMERO Q ESCRIBIO LA PERSONA(adivinanza) ES MENOR AL NUMERO SECRETO
                print(f"El numero secreto es mayor a {adivinanza}") 
            elif adivinanza > numero_secreto:                           #elif q pasa lo contrario
                print(f"El numero secreto es menor a {adivinanza}") 
            else:
                print(f"Felicitaciones has ganado wachin! EL numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos. ")
        else:
            print("Por favor introduzca un numero valido entre el 1 al 100") #esto es si no pusieron un numero entre el 1 al 100. va debajo del IF principal.

juego_adivinanza() 

