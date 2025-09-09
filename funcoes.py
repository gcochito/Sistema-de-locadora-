import os 

from classes import *

locaSenai = Locadora()


def cadastro():
    while True:
        print("-Cadastro-")
        cada=int(input("O que você deseja cadastrar? \n 1. Cliente \n 2. Item \n ->"))
        match cada:
            case 1:
                nome = input("Informe seu nome:")
                cpf = ("Informe seu CPF:")
                locaSenai.cadastrarCliente[Cliente(nome=nome, cpf=cpf)]
                print("Cliente Adicionado ")
            case 2:
                codigo = input("Informe o código: ")
                titulo = input("Informe o titulo:")
                locaSenai.cadastrarItem(codigo=codigo, titulo=titulo)

def listar ():
    while True:
        print("-Listar-")
        li=int(input("O que você deseja listar? \n 1. Clientes \n 2. Itens \n ->"))
        match li:
            case 1:
                for chave, valor in locaSenai.listar().items():
                    print(f"{chave}° - \t{valor.getNome()} \n \t{valor.getCpf()}")
    
            case 2:
                for chave, valor in locaSenai.listar().items():
                    print(f"{chave}° - \t{valor.Codigo()} \n \t{valor.getTitulo()}")


def alugar ():
    while True:
        print("-Alugar-")
        listar(cliente, item)
        cliente_id = int(input("Digite o ID do cliente: "))
        item_id = int(input("Digite o ID do item: "))
        cliente = locaSenai.getClientes().get(cliente_id)
        item = locaSenai.getItens().get(item_id)
        locaSenai.aluga (cliente, item)


def devolver ():
    while True:
        print("-Devolver-")
        listar(cliente, item)
        cliente_id = int(input("Digite o ID do cliente: "))
        item_id = int(input("Digite o ID do item: "))
        cliente = locaSenai.getClientes().get(cliente_id)
        item = locaSenai.getItens().get(item_id)
        locaSenai.devolver (cliente)


