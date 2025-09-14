import os 

from classes import *

locaSenai = Locadora()


def cadastro():
    while True:
        print("-Cadastro-")
        cada=int(input("O que você deseja cadastrar? \n 0. Sair \n 1. Cliente \n 2. Item \n ->"))
        match cada:
            case 1:
                nome = input("Informe seu nome:")
                cpf = input ("Informe seu CPF:")
                cliente= Cliente(nome, cpf)
                locaSenai.cadastrarCliente(cliente)
                print("Cliente Adicionado ")
                os.system("pause")
            case 2:
                codigo = input("Informe o código: ")
                titulo = input("Informe o titulo:")
                item= Item(codigo,titulo)
                locaSenai.cadastrarItem(item)
                print("Item adicionado")
                os.system("pause")
            case 0:
                break
            case _:
                print("Opção inválida")
                os.system("pause")

def listar ():
    while True:
        print("-Listar-")
        li=int(input("O que você deseja listar? \n 0.Sair \n 1. Clientes \n 2. Itens \n ->"))
        match li:
            case 1:
                for chave, valor in locaSenai.listar().items():
                    print(f"{chave}° - \t{valor.getNome()} \n \t{valor.getCpf()}")
    
            case 2:
                for chave, valor in locaSenai.listar().items():
                    print(f"{chave}° - \t{valor.getCodigo()} \n \t{valor.getTitulo()}")
            case 0:
                break
            case _:
                print("Opção inválida!")
                os.system("pause")

def alugar ():
    while True:
        print("-Alugar-")
        listar()
        cliente_id = int(input("Digite o ID do cliente: "))
        item_id = int(input("Digite o ID do item: "))
        cliente = locaSenai.getClientes()[cliente_id]
        item = locaSenai.getItens()[item_id]
        cliente.locar(item)
        print(f"{cliente.getNome()} alugou {item.getTitulo()}")
        os.system("pause")


def devolver ():
    while True:
        print("-Devolver-")
        listar()
        cliente_id = int(input("Digite o ID do cliente: "))
        item_id = int(input("Digite o ID do item: "))
        cliente = locaSenai.getClientes()[cliente_id]
        item = locaSenai.getItens()[item_id]
        cliente.devolver (item)
        print(f"{cliente.getNome()} devolveu {item.getTitulo()}")
        os.system("pause")



