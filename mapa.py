class ElementoUnicoDaLista:
    def __init__(self, elemento):
        self.elementoDaLista = elemento
        self.proximoElemento = None

class Produto:
    def __init__(self, nome, unidade, custo, venda):
        self._nome = nome
        self.unidade = unidade
        self.custo = custo
        self.venda = venda

    def __repr__(self):
        return "{}".format(self._nome, self.unidade, self.custo, self.venda)

class ListaLigada:
    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def inserirNoInicioLista(self, conteudo):
        elemento = ElementoUnicoDaLista(conteudo)
        elemento.proximoElemento = self._inicio
        self._inicio = elemento
        self._quantidade += 1

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            self.inserirNoInicioLista(conteudo)
            return
        elemento = ElementoUnicoDaLista(conteudo)
        esquerda = self._elemento(posicao - 1)
        elemento.proximoElemento = esquerda.proximoElemento
        esquerda.proximoElemento = elemento
        self._quantidade += 1

    def _elemento(self, posicao):
        self._validarPosicao(posicao)
        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximoElemento
        return atual

    def _validarPosicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida {posicao}")


    def imprimir(self):
        atual = self.inicio
        print("PRODUTOS")
        print("--------\n")
        for i in range(0, self.quantidade):
            lucro = (atual.elementoDaLista.unidade * atual.elementoDaLista.venda) - (atual.elementoDaLista.unidade * atual.elementoDaLista.custo)
            print("Nome do produto: {}, unidades: {}, valor de custo: R$ {}, valor de venda: R$ {}, lucro esperado: R$ {:.2f}".format(atual.elementoDaLista, atual.elementoDaLista.unidade, atual.elementoDaLista.custo, atual.elementoDaLista.venda, lucro))
            atual = atual.proximoElemento



def main():
    produto1 = Produto("Arroz", 5, 8.54, 13.99)
    produto2 = Produto("Feijão", 4, 3.35, 7.00)
    produto3 = Produto("Óleo de Soja", 7, 6.21, 9.00)
    produto4 = Produto("Molho de tomate", 10, 1.00, 3.25)
    produto5 = Produto("Macarrão parafuso", 8, 1.25, 4.75)
    produto6 = Produto("Sal", 3, 2.00, 4.00)
    lista = ListaLigada()
    lista.inserirNoInicioLista(produto1)
    lista.inserirNoInicioLista(produto2)
    lista.inserirNoInicioLista(produto3)
    lista.inserir(1, produto4)
    lista.inserir(0, produto5)
    lista.inserir(lista.quantidade, produto6)
    print("-------------------------------------")
    print("Quantidade de produtos registrados: {}".format(lista.quantidade))
    print("-------------------------------------\n")
    lista.imprimir()
main()