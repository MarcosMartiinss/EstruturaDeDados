def conjunto():
    primeiroSet = {6, "Dez", 4}  # Criando um set
    print("Conjunto:", primeiroSet)
    print("------------------------------")

    primeiroSet.add("Um")
    print("Adicionando um elemento ao conjunto:", primeiroSet)
    print("------------------------------")

    primeiroSet.remove("Dez")  # caso não exista, o condigo vai lançar um erro
    print("Exemplo de set com remove:", primeiroSet)
    print("------------------------------")

    primeiroSet.discard("Dez")  # Ele remove um elemento, caso o elemento não exist, ele não lançará nenhum erro
    print("Exemplo de set com discard:", primeiroSet)
    print("------------------------------")

    print("Tamanho do conjunto:", len(primeiroSet))
    print("------------------------------")

    segundoSet = {3.2, 4, True, "Novo", 20, 5, "Um"}

    uniao = primeiroSet.union(segundoSet)  # Unindo 2 set e atribuindo a um terceiro
    print("União:", uniao)
    print("------------------------------")

    intersecao = primeiroSet.intersection(segundoSet)  # Cria um set com a intersecção de outros dois
    print("Intersecção:", intersecao)
    print("------------------------------\n")


conjunto()

''' No python existe o frozenset, a única diferença entre os dois é que o frozenset é imutável'''

print("FROZEN SET")
print("----------\n")


def conjuntoImutavel():
    listaUm = ["maçã", "banana", "morango"]
    print("Exemplo da listaUm:", listaUm)
    print("------------------------------")

    conjuntoCongeladoUm = frozenset(listaUm)
    print("Exemplo conjuntocongeladoum:", conjuntoCongeladoUm)
    print("------------------------------")

    conjuntoCongeladoDois = {"Gui", 34, True, 40, "masculino"}
    print("Conjunto dois congelado:", conjuntoCongeladoDois)
    print("------------------------------")

    contador = 1
    for extracao in conjuntoCongeladoDois:
        print(f"Extraindo elementos {contador}", extracao)
        contador += 1
    print("------------------------------")


conjuntoImutavel()
