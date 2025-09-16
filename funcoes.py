import os 

from classes import *

locaSenai = Locadora()


def cadastro():
    while True:
        try:
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
                    tipo= int(input("Informe o tipo de item: \n1. Filme \n2. Jogo \n-> "))
                    codigo = input("Informe o código: ")
                    titulo = input("Informe o titulo:")
                    match tipo:
                        case 1:
                            genero = input("Informe o gênero: ")
                            duracao = input("Informe a duração (em minutos): ")
                            item = Filme(codigo, titulo, genero, duracao)
                            print("Filme adicionado")
                        case 2:
                            plataforma = input("Informe a plataforma: ")
                            faixaEtaria=int(input("Informe a Faixa Etaria:"))
                            item = Jogo(codigo, titulo, plataforma, faixaEtaria)
                            print("Jogo adicionado")
                    locaSenai.cadastrarItem(item)
                    print("Item adicionado")
                    os.system("pause")
                case 0:
                    break
                case _:
                    print("Opção inválida")
                    os.system("pause")
        except ValueError:
            print("Erro: Digite apenas números!")
            os.system("pause")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")

def listar ():
    while True:
        try:
            print("-Listar-")
            li=int(input("O que você deseja listar? \n 0.Sair \n 1. Clientes \n 2. Itens \n ->"))
            match li:
                case 1:
                    count=1
                    for cliente in locaSenai.listarClientes():
                        print(f"ID:{count} \n Nome: {cliente.getNome()} \n CPF: {cliente.getCpf()} \n Itens locados: {cliente.getItensLocados()}")
                        count+=1
                case 2:
                    count=1
                    for itens in locaSenai.listarItens():
                        print(f" ID:{count} \n Código: {itens.getCodigo()} \n Titulo: {itens.getTitulo()}")
                        count+=1
                case 0:
                    break
                case _:
                    print("Opção inválida!")
                    os.system("pause")
        except ValueError:
            print("Erro: Digite apenas números!")
            os.system("pause")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")
def alugar ():
    while True:
        try:
            print("-Alugar-")
            print("\nClientes cadastrados:")
            count = 1
            for cliente in locaSenai.listarClientes():
                print(f"ID:{count} \n Nome: {cliente.getNome()} \n CPF: {cliente.getCpf()}")
                count += 1
            print("\nItens disponíveis:")
            count = 1
            for item in locaSenai.listarItens():
                match item.getDisponivel():
                    case True:
                        disponivel = "Disponível"
                    case False:
                        disponivel = "Alugado"
                print(f"ID:{count} \n Titulo: {item.getTitulo()} \n Status: {disponivel}")
                count += 1
            cliente_id = int(input("\nDigite o ID do cliente: "))
            item_id = int(input("Digite o ID do item: "))
            cliente = locaSenai.getClientes()[cliente_id - 1]
            item = locaSenai.getItens()[item_id - 1]
            match item.getDisponivel():
                case True:
                    cliente.locar(item)
                    item.setDisponivel(False)
                    print(f"{cliente.getNome()} alugou {item.getTitulo()}")
                case False:
                    print("Esse item já está alugado")
            os.system("pause")
            break 

        except ValueError:
            print("Erro: Digite apenas números válidos!")
            os.system("pause")
        except IndexError:
            print("Erro: ID inválido! Verifique os números digitados.")
            os.system("pause")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")    

def devolver ():
    while True:
        try:
            print("-Devolver-")
            print("Clientes cadastrados:")
            count = 1
            for cliente in locaSenai.listarClientes():
                print(f"ID:{count} \nNome: {cliente.getNome()} \n CPF: {cliente.getCpf()}")
                count += 1
            
            print("\nItens:")
            count = 1
            for item in locaSenai.listarItens():
                match item.getDisponivel():
                    case True:
                        disponivel = "Disponível"
                    case False:
                        disponivel = "Alugado"
                print(f"ID:{count} \n Titulo: {item.getTitulo()} \n Status: {disponivel}")
                count += 1

            cliente_id = int(input("\nDigite o ID do cliente: "))
            item_id = int(input("Digite o ID do item: "))
            
            cliente = locaSenai.getClientes()[cliente_id - 1]
            item = locaSenai.getItens()[item_id - 1]
            
            match item in cliente.getItensLocados():
                case True:
                    cliente.devolver(item)
                    item.setDisponivel(True)
                    print(f"{cliente.getNome()} devolveu {item.getTitulo()}")
                case False:
                    print(f"O cliente {cliente.getNome()} não tem esse item alugado.")
            
            os.system("pause")
            break
        
        except ValueError:
            print("Erro: Digite apenas números válidos!")
            os.system("pause")
        except IndexError:
            print("Erro: ID inválido! Verifique os números digitados.")
            os.system("pause")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")
        