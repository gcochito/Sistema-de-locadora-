import os

from funcoes import *

while True:
    os.system("cls")
    print("Bem vindo ao sistema de locação")
    print("Selecione um opção")
    print("1. Cadastro ")
    print("2 ")
    print("3. ")
    print("0. Sair")
    escolha= int(input("->"))

    match escolha:
        case 1:
            cadastro()
        case 2:
            listar ()

        case 3:
            pass

        case 4:
            pass

        case 0:
            print("Saindo...")
            os.system("pause")
            break
        case _:
            print("Escolha Invalida")
            os.system("pause")


