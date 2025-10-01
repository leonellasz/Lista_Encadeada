import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0  
    def esta_vazia(self):
        return self.tamanho == 0

    def tamanho(self):
        return self.tamanho 

    
    def _obter_no_na_posicao(self, posicao):
        """Método auxiliar para encontrar um nó em uma posição."""
        if not (1 <= posicao <= self.tamanho):
            return None

        atual = self.inicio
        for _ in range(posicao - 1):
            atual = atual.proximo
        return atual

    def obter_elemento(self, posicao):
        no = self._obter_no_na_posicao(posicao)  
        if no:
            return no.valor
        return None

    def modificar_elemento(self, posicao, novo_valor):
        no = self._obter_no_na_posicao(posicao)  
        if no:
            no.valor = novo_valor
            return True
        return False

    def inserir(self, posicao, valor):
        if not (1 <= posicao <= self.tamanho + 1):
            return False

        novo_no = No(valor)
        if posicao == 1:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
           
            anterior = self._obter_no_na_posicao(posicao - 1)
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no

        self.tamanho += 1  # <-- MELHORIA 1: Atualiza o tamanho
        return True

    def remover(self, posicao):
        if self.esta_vazia() or not (1 <= posicao <= self.tamanho):
            return False

        if posicao == 1:
            self.inicio = self.inicio.proximo
        else:
           
            anterior = self._obter_no_na_posicao(posicao - 1)
            no_a_remover = anterior.proximo
            anterior.proximo = no_a_remover.proximo

        self.tamanho -= 1  # <-- MELHORIA 1: Atualiza o tamanho
        return True

  
    def __str__(self):
       
        if self.esta_vazia():
            return "Lista vazia."

        resultado = ""
        atual = self.inicio
        while atual:
            resultado += f"{atual.valor} -> "
            atual = atual.proximo
        resultado += "None"
        return resultado

    def imprimir(self):
        
        print(self)

    def salvar_em_arquivo(self, nome_arquivo="lista.txt"):
        with open(nome_arquivo, "w") as f:
            atual = self.inicio
            while atual:
                f.write(f"{atual.valor}\n")
                atual = atual.proximo

    def carregar_de_arquivo(self, nome_arquivo="lista.txt"):
        self.inicio = None
        self.tamanho = 0  # <-- MELHORIA 1: Reseta o tamanho ao carregar
        if not os.path.exists(nome_arquivo):
            return
        with open(nome_arquivo, "r") as f:
            # A inserção já atualiza o tamanho, não precisamos contar aqui
            linhas = [linha.strip() for linha in f if linha.strip().isdigit()]
        for i, linha in enumerate(linhas):
            self.inserir(i + 1, int(linha))


# ===============================
# CASOS DE TESTE AUTOMÁTICOS
# ===============================
def casos_de_teste():
    print("=========== CASOS DE TESTE AUTOMÁTICOS ===========")
    lista = ListaEncadeada()

    print("Lista inicialmente vazia:", lista.esta_vazia())

    print("\nInserindo valores:")
    lista.inserir(1, 10)
    lista.inserir(2, 20)
    lista.inserir(2, 15)
    lista.imprimir()  # ou print(lista)

    print("\nTamanho da lista:", lista.tamanho)

    print("\nValor na posição 2 (esperado 15):", lista.obter_elemento(2))

    print("\nModificando valor da posição 2 para 99...")
    lista.modificar_elemento(2, 99)
    lista.imprimir()

    print("\nRemovendo elemento da posição 1...")
    lista.remover(1)
    lista.imprimir()

    print("=========== FIM DOS TESTES ===========")
    input("\nPressione Enter para continuar para o menu...")


# ===============================
# MENU INTERATIVO 
# ===============================
def menu():
    lista = ListaEncadeada()
    lista.carregar_de_arquivo()

    while True:
        limpar_tela()
        print("--- MENU DA LISTA ENCADEADA (VERSÃO OTIMIZADA) ---")
        print(f"Estado Atual: {lista}\n")  # <-- MELHORIA 3: Usando print(lista)
        print("1. Verificar se a lista está vazia")
        print("2. Obter tamanho da lista")
        print("3. Obter valor de uma posição")
        print("4. Modificar valor de uma posição")
        print("5. Inserir elemento em uma posição")
        print("6. Remover elemento de uma posição")
        print("7. Imprimir a lista (demonstração)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        limpar_tela()

        if opcao == '1':
            print("A lista está vazia?", lista.esta_vazia())
        elif opcao == '2':
            print("Tamanho da lista:", lista.tamanho)
        elif opcao == '3':
            try:
                pos = int(input("Digite a posição (1 até N): "))
                valor = lista.obter_elemento(pos)
                print("Valor na posição", pos, ":", valor if valor is not None else "posição inválida")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número.")
        elif opcao == '4':
            try:
                pos = int(input("Digite a posição a modificar: "))
                novo = int(input("Digite o novo valor: "))
                if lista.modificar_elemento(pos, novo):
                    print("Valor modificado com sucesso!")
                    lista.salvar_em_arquivo()
                else:
                    print("Erro: posição inválida.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número.")
        elif opcao == '5':
            try:
                pos = int(input("Digite a posição de inserção: "))
                val = int(input("Digite o valor a inserir: "))
                if lista.inserir(pos, val):
                    print("Valor inserido com sucesso.")
                    lista.salvar_em_arquivo()
                else:
                    print("Erro: posição inválida.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número.")
        elif opcao == '6':
            try:
                pos = int(input("Digite a posição a remover: "))
                if lista.remover(pos):
                    print("Elemento removido com sucesso.")
                    lista.salvar_em_arquivo()
                else:
                    print("Erro: posição inválida.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número.")
        elif opcao == '7':
            print("Elementos da lista:")
            lista.imprimir()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")


# execução principal
if __name__ == "__main__":
    # casos_de_teste() #  descomentar esta linha para rodar os testes antes do menu
    menu()
