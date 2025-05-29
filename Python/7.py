# 🟢 7. Verificador de Palíndromo: Verifique se uma palavra é um palíndromo (ex.: arara).

palavra = input("Digite uma palavra para verificar se é um palíndromo: ").strip().lower()
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:   
    print(f"A palavra '{palavra}' não é um palíndromo.")