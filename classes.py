class Item():
    def __init__(self,codigo, titulo):
        self.__codigo= codigo
        self.__titulo = titulo
        self.__disponivel = True

    def getCodigo(self):
        return self.__codigo

    def getTitulo(self):
        return self.__titulo

    def getDisponivel(self):
        return self.__disponivel

    def setTitulo(self, titulo):
        self.__titulo = titulo
        return self.__titulo

    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel
        return self.__disponivel
    
    def alugar(self):
        self.__disponivel = False

    
    def devolver(self):
        self.__disponivel = True
    
    
class Filme (Item):
    def __init__(self, codigo, titulo, genero, duracao):
        super().__init__(codigo, titulo)
        self.__genero = genero 
        self.__duracao = duracao
        
        def getGenero(self):
            return self.__genero 
        
        def getDuracao(self):
            return self.__duracao 
        

class Jogo (Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        super().__init__(codigo, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

        def getPlataforma(self):
            return self.__plataforma
        
        def getfaixaEtaria(self):
            return self.__faixaEtaria
       



class Cliente():
    def __init__(self, nome, cpf):
        self.__nome=nome 
        self.__cpf=cpf
        self.__itensLocados = []

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getItensLocados(self):
        return self.__itensLocados

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome

    def setCpf(self, cpf):
        self.__cpf = cpf
        return self.__cpf

    def locar(self, item):
        item.alugar()
        self.__itensLocados.append(item)
    
    def devolver(self, item):
        item.devolver()
        self.__itensLocados.remove(item)

    def listarItens (self):
        return self.__itensLocados


class Locadora():
    def __init__(self):
        self.__clientes=[]
        self.__itens=[]

    def cadastrarCliente (self, cliente):
        self.__clientes.append(cliente)

    def cadastrarItem (self, item):
        self.__itens.append(item)

    
    def listarClientes(self):
        return self.__clientes


    def listarItens (self):
        return self.__itens
    
    def getClientes(self):
        return self.__clientes

    def getItens(self):
        return self.__itens

