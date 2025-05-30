import os

# Diretórios / extensões
diretorios_extensoes = {
    r"C:\Users\User\Documents\Desafio-dos-50\C++": ".cpp",
    r"C:\Users\User\Documents\Desafio-dos-50\Java": ".java",
    r"C:\Users\User\Documents\Desafio-dos-50\JavaScript": ".js",
    r"C:\Users\User\Documents\Desafio-dos-50\Julia": ".jl",
    r"C:\Users\User\Documents\Desafio-dos-50\Kotlin": ".kt",
    r"C:\Users\User\Documents\Desafio-dos-50\Rust": ".rs",
    r"C:\Users\User\Documents\Desafio-dos-50\Python": ".py",
}

# Conteúdo básico (opcional, pode ser personalizado)
conteudo_por_extensao = {
    ".cpp": '#include <iostream>\n\nint main() {\n    std::cout << "Olá, mundo!\\n";\n    return 0;\n}',
    ".java": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Olá, mundo!");\n    }\n}',
    ".js": "console.log('Olá, mundo!');",
    ".jl": 'println("Olá, mundo!")',
    ".kt": 'fun main() {\n    println("Olá, mundo!")\n}',
    ".rs": 'fn main() {\n    println!("Olá, mundo!");\n}',
    ".py": "print('Olá, mundo!')",
}

# Cria os arquivos em cada diretório
for diretorio, extensao in diretorios_extensoes.items():
    os.makedirs(diretorio, exist_ok=True)  # Garante que o diretório existe

    # Verifica existentes
    arquivos_existentes = os.listdir(diretorio)
    ultimo_numero = 0

    for arquivo in arquivos_existentes:
        if arquivo.endswith(extensao) and arquivo[: -len(extensao)].isdigit():
            numero = int(arquivo[: -len(extensao)])
            if numero > ultimo_numero:
                ultimo_numero = numero

    # Cria os arquivos faltantes (do próximo número até 50)
    for i in range(ultimo_numero + 1, 51):
        nome_arquivo = os.path.join(diretorio, f"{i}{extensao}")
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(
                conteudo_por_extensao.get(extensao, "")
            )  # Insere conteúdo padrão

    print(f"[OK] {diretorio}: criados {50 - ultimo_numero}).")

print("\nConcluído!")
