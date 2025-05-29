# 🟢 5. Tabuada: Mostre a tabuada de um número informado pelo usuário.
numero = int(input("Digite um número para ver sua tabuada: "))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for _ in lista:
    resultado = numero * _
    print(f"{numero} x {_} = {resultado}")
