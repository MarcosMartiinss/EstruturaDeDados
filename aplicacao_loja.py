from lista_ligada import ListaLigada, ElementoUnicoDaLista


class Loja:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self._nome, self._endereco)

def main():
    loja1 = Loja("Mercadinho do Zé", "Rua das frutas frscas, 1234")
    loja2 = Loja("Direto do colono", "Rua do colono, 10000")
    loja3 = Loja("Quitanda do Bairro", "Rua cds Cebolas, 9999")
    loja4 = Loja("Boa Fruta", "Rua Eureka, 13254")
    loja5 = Loja("Horti Agora", "Rua da Praia, 5464")
    loja6 = Loja("Fruti-Fruti", "Av. dos Verdes, 5")
    lista = ListaLigada()
    lista.inserirNoInicioLista(loja1)
    lista.inserirNoInicioLista(loja2)
    lista.inserirNoInicioLista(loja3)
    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)
    print(lista.quantidade)
    lista.imprimir()
    removido = lista.removerDoInicio()
    print(lista.quantidade)
    print(f"Removido: {removido}")
    print("\n")
    print(lista.quantidade)
    lista.imprimir()
    print("----------")
    print("elemento removido {}".format(lista.remover(2)))
    print("\n")
    print(lista.quantidade)
    lista.imprimir()
    print("\n\nEncontrando o elemento 2: {}".format(lista.buscaElemento(1)))

main()