# Gerenciador de Tarefas do Estagiário
tarefas = []

while True:
    print("\n--- MEU GERENCIADOR DE ESTUDOS ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nova_tarefa = input("Qual tecnologia você vai estudar hoje? ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        print("\nSUAS TAREFAS:")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
    elif opcao == "3":
        print("Foco nos estudos! Saindo...")
        break
    else:
        print("Opção inválida!")
