from elemento_lista import ElementoUnicoDaLista


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

    def removerDoInicio(self):
        removido = self.inicio
        self._inicio = removido.proximoElemento
        removido.proximoElemento = None
        self._quantidade -= 1
        return removido.elementoDaLista

    def remover(self, posicao):
        esquerda = self._elemento(posicao - 1)
        removido = esquerda.proximoElemento
        esquerda.proximoElemento = removido.proximoElemento
        removido.proximoElemento = None
        self._quantidade -= 1
        return removido.elementoDaLista

    def buscaElemento(self, posicao):
        self._validarPosicao(posicao)
        elemento = self._elemento(posicao)
        return elemento.elementoDaLista

    def imprimir(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.elementoDaLista)
            atual = atual.proximoElemento