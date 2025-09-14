import os

from funcoes import *

while True:
    try:
        os.system("cls")
        print("Bem vindo ao sistema de locação")
        print("Selecione um opção")
        print("1. Cadastro ")
        print("2. Listar ")
        print("3. Alugar ")
        print("4. Devolver")
        print("0. Sair")
        escolha= int(input("->"))

        match escolha:
            case 1:
                cadastro()
            case 2:
                listar ()

            case 3:
                alugar()

            case 4:
                devolver()

            case 0:
                print("Saindo...")
                os.system("pause")
                break
            case _:
                print("Escolha Invalida")
                os.system("pause")

    except ValueError:
        print("Erro: Digite apenas números!")
        os.system("pause")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        os.system("pause")
