# 🟢 6. Fatorial Simples: Calcule o fatorial de um número inteiro positivo.
numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

if numero < 0:
    print("Fatorial não definido para números negativos.")
elif numero == 0 or numero == 1:
    print(f"O fatorial de {numero} é 1.")
else:
    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")