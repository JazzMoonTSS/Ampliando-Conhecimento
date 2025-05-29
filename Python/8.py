# 🟢 8. Contador de Vogais: Conte quantas vogais há em uma string.

string = input("Digite uma string para contar as vogais: ").strip().lower()
vogais = "aeiou"
contagem = sum(1 for _ in string if _ in vogais)
print(f"A string '{string}' contém {contagem} vogais.")