# 🟢 2. Par ou Ímpar: Receba um número e diga se é par ou ímpar.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")