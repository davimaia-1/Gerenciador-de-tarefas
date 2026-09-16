ARQUIVO = "medicamentos.txt"

def salvar(medicamentos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for m in medicamentos:
            arquivo.write(f"{m['nome']};{m['categoria']};{m['quantidade']}\n")

def carregar():
    medicamentos = []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, categoria, quantidade = linha.strip().split(";")
                medicamentos.append({
                    "nome": nome,
                    "categoria": categoria,
                    "quantidade": int(quantidade)
                })
    except FileNotFoundError:
        pass

    return medicamentos


medicamentos = carregar()

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        quantidade = int(input("Quantidade: "))

        medicamentos.append({
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade
        })

        print("Cadastrado!")

    elif opcao == "2":
        for m in medicamentos:
            print(f"{m['nome']} - {m['categoria']} - {m['quantidade']}")

    elif opcao == "3":
        nome = input("Nome para buscar: ")

        for m in medicamentos:
            if m["nome"].lower() == nome.lower():
                print(f"Nome: {m['nome']}")
                print(f"Categoria: {m['categoria']}")
                print(f"Quantidade: {m['quantidade']}")
                break
        else:
            print("Não encontrado.")

    elif opcao == "4":
        salvar(medicamentos)
        print("Dados salvos!")
        break

    else:
        print("Opção inválida.")
