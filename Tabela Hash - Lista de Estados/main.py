#Definindo a classe Nodo
class Nodo:
    def __init__(self, sigla):
        self.sigla = sigla #Armazena sigla de cada estado
        self.proximo = None #Próximo nodo

class TabelaHash: #Criando tabela Hash
    def __init__(self):
        self.tabela = [None] * 10 #Inicia a tabela em None caso o usuário solicite a opção 3 (Listar a tabela Hash)

    def funcao_hash(self, sigla): #Função para inserir o DF na posição 7 conforme solicitado
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla): #Insere uma nova sigla cada vez que o usuario solicita para inserir na tabela
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla)
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_nodo #Insere None se estiver vazio
        else:
            novo_nodo.proximo = self.tabela[indice] #Insere o novo nodo
            self.tabela[indice] = novo_nodo

    def remover(self, sigla): #Remoção da sigla inserida
        indice = self.funcao_hash(sigla)
        atual = self.tabela[indice]
        anterior = None #Mantém o nodo anterior
        while atual is not None and atual.sigla != sigla:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            print(f"Sigla {sigla} não encontrada.")
            return
        if anterior is None:
            self.tabela[indice] = atual.proximo # Se o nodo for o primeiro a ser removifo, ajusta o ponteiro da tabela
        else:
            anterior.proximo = atual.proximo ##Se não for o primeiro, ajusta o nodo anterior
        print(f"Sigla {sigla} removida.")

    def listar(self): #Listagem da tabela Hash
        for i in range(len(self.tabela)):
            print(f"{i}: ", end="")  #Índice a tabela (até 9) (Função Hash já definida até 10 (Um a mais)
            atual = self.tabela[i] #Primeiro nodo da lista
            if atual is None:
                print("None") #Imprime None na vazia, conforme pedido
            else:
                while atual is not None: #Imprime a sigla inserida e o ponteiro
                    print(f"{atual.sigla}", end=" -> ")
                    atual = atual.proximo
                print("None")

tabela_hash = TabelaHash()

while True:
    print("1 - Inserir na tabela Hash")
    print("2 - Remover da tabela Hash")
    print("3 - Listar a tabela Hash")
    print("4 - SAIR")

    op = int(input("\nEscolha uma opção: "))
    if op == 1:
        sigla = input("Digite a sigla de um estado: ").upper()
        tabela_hash.inserir(sigla)
    elif op == 2:
        sigla = input("Digite a sigla do estado a ser removido: ").upper()
        tabela_hash.remover(sigla)
    elif op == 3:
        print("\nTabela Hash:")
        tabela_hash.listar()
    elif op == 4:
        print("Finalizando programa...")
        break
    else:
        print("Opção Inválida!\n")
