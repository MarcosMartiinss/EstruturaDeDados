def referencia(novaLista):
    novaLista[1] = "novo valor"


def ponteiro():
    lista = []  # criar lista vazia
    print("Tamanho da lista", len(lista))

    lista = ['O carro', 'peixe', 123, 111]  # criando lista com os elementos

    for elemento in lista:
        print("Original:", elemento)

    referencia(lista)  # chamando a referência
    print("----------")

    for elemento in lista:
        print("Teste:", elemento)


ponteiro()
