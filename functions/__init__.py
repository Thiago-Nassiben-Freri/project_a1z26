# functions.py

from time import sleep

def exit():
    print('Ok, saindo')
    sleep(2)
    print('Programa encerrado!')

def cryptographerA1Z26(msg): 
    numeros = []
    for letra in msg: 
        if letra.isalpha(): 
            numero = str(ord(letra.lower()) - ord('a') + 1) 
            numeros.append(numero)
        else: 
            numeros.append(letra)
    return ''.join(map(str, numeros))

