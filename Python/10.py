# 🟢 10. Soma dos Pares: Some todos os números pares de 1 a N.
import random

def feedback(arg,lista,res):
    if arg == True:
        print(f"O resultado da soma dos números pares da lista {lista} é {res}!")
    else:
        print(f"A lista {lista} não tem números pares!")

def somar_pares():

    lista = []
    _ = 0
    resultado = 0

    for _ in range(10):

        numeros = random.randint(1, 100)
        lista.append(numeros)

    for _ in lista:

        if _ % 2 == 0:
            resultado = resultado + _
    
    if resultado == 0:

        feedback(False,lista,resultado)

    else:

        feedback(True,lista,resultado)
            
somar_pares()