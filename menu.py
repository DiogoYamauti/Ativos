import requests
import os
import platform

BASE_URL = "http://127.0.0.1:5000"

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display_message(response):
    order = ["cpf", "nome", "notebook", "monitor1", "monitor2", "teclado", "mouse", "desktop", "acessorios", "nobreak", "headset", "celular"]
    try:
        json_response = response.json()
        if response.status_code == 200 or response.status_code == 201:
            if isinstance(json_response, list):
                for item in json_response:
                    ordered_data = {key: item.get(key) for key in order if key in item}
                    print("\n".join([f"{key}: {value}" for key, value in ordered_data.items()]))
                    print("-" * 40)
            else:
                ordered_data = {key: json_response.get(key) for key in order if key in json_response}
                print("\n".join([f"{key}: {value}" for key, value in ordered_data.items()]))
        else:
            print(json_response.get("error", "Erro desconhecido"))
    except ValueError:
        print("Erro: não foi possível decodificar a resposta JSON")
    except Exception as e:
        print(f"Erro ao processar a resposta: {e}")

def menu():
    while True:
        clear_console()
        print("\nMenu:")
        print("1. Inserir um novo funcionário")
        print("2. Excluir um funcionário")
        print("3. Listar todos os funcionários")
        print("4. Consultar o inventário completo de um determinado funcionário")
        print("5. Atualizar o nome do funcionário")
        print("6. Atualizar ativos de um funcionário")
        print("7. Limpar ativos de um funcionário")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        clear_console()

        if opcao == '1':
            cpf = input("CPF: ")
            nome = input("Nome: ")
            dados = {
                "cpf": cpf,
                "nome": nome,
                "notebook": None,
                "monitor1": None,
                "monitor2": None,
                "teclado": None,
                "mouse": None,
                "nobreak": None,
                "desktop": None,
                "headset": None,
                "celular": None,
                "acessorios": None
            }
            response = requests.post(f"{BASE_URL}/funcionarios", json=dados)
            display_message(response)

        elif opcao == '2':
            cpf = input("CPF do funcionário a ser excluído: ")
            response = requests.delete(f"{BASE_URL}/funcionarios/{cpf}")
            display_message(response)

        elif opcao == '3':
            response = requests.get(f"{BASE_URL}/funcionarios")
            display_message(response)

        elif opcao == '4':
            cpf = input("CPF do funcionário: ")
            response = requests.get(f"{BASE_URL}/funcionarios/{cpf}")
            display_message(response)

        elif opcao == '5':
            cpf = input("CPF do funcionário: ")
            nome = input("Novo nome: ")
            dados = {"nome": nome}
            response = requests.put(f"{BASE_URL}/funcionarios/{cpf}", json=dados)
            display_message(response)

        elif opcao == '6':
            cpf = input("CPF do funcionário: ")
            print("Digite os ativos que deseja atualizar (deixe em branco para pular):")
            notebook = input("Notebook: ")
            monitor1 = input("Monitor 1: ")
            monitor2 = input("Monitor 2: ")
            teclado = input("Teclado: ")
            mouse = input("Mouse: ")
            nobreak = input("Nobreak: ")
            desktop = input("Desktop: ")
            headset = input("Headset: ")
            celular = input("Celular: ")
            acessorios = input("Acessórios: ")
            dados = {}
            if notebook:
                dados["notebook"] = notebook
            if monitor1:
                dados["monitor1"] = monitor1
            if monitor2:
                dados["monitor2"] = monitor2
            if teclado:
                dados["teclado"] = teclado
            if mouse:
                dados["mouse"] = mouse
            if nobreak:
                dados["nobreak"] = nobreak
            if desktop:
                dados["desktop"] = desktop
            if headset:
                dados["headset"] = headset
            if celular:
                dados["celular"] = celular
            if acessorios:
                dados["acessorios"] = acessorios

            response = requests.put(f"{BASE_URL}/funcionarios/{cpf}/ativos", json=dados)
            display_message(response)

        elif opcao == '7':
            cpf = input("CPF do funcionário: ")
            print("Digite os ativos que deseja limpar (deixe em branco para pular):")
            notebook = input("Notebook: ")
            monitor1 = input("Monitor 1: ")
            monitor2 = input("Monitor 2: ")
            teclado = input("Teclado: ")
            mouse = input("Mouse: ")
            nobreak = input("Nobreak: ")
            desktop = input("Desktop: ")
            headset = input("Headset: ")
            celular = input("Celular: ")
            acessorios = input("Acessórios: ")
            dados = {}
            if notebook:
                dados["notebook"] = notebook
            if monitor1:
                dados["monitor1"] = monitor1
            if monitor2:
                dados["monitor2"] = monitor2
            if teclado:
                dados["teclado"] = teclado
            if mouse:
                dados["mouse"] = mouse
            if nobreak:
                dados["nobreak"] = nobreak
            if desktop:
                dados["desktop"] = desktop
            if headset:
                dados["headset"] = headset
            if celular:
                dados["celular"] = celular
            if acessorios:
                dados["acessorios"] = acessorios

            response = requests.delete(f"{BASE_URL}/funcionarios/{cpf}/ativos", json=dados)
            display_message(response)

        elif opcao == '8':
            break

        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu()
