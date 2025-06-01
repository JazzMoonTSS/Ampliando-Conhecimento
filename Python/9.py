# 🟢 9. Média Aritmética: Receba uma lista de números e calcule a média.

def solicitar_lista():
    numeros = input("Digite uma lista de números separados por vírgula (Exemplo: 7.5, 10, 6.5, 5): ")

    if not numeros:
        solicitar_lista()
    else:
        numeros = [float(_) for _ in numeros.split(",")]
        media = sum(numeros) / len(numeros)
        
        print(f"A média dos números é: {media}")

solicitar_lista()
