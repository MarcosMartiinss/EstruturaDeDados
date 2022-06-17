def tuplaInicio():
    primeiraTupla = (1, 3, "Teste", 0.4)  # definindo a tupla
    print("Primeira tupla:", primeiraTupla)
    print("-----------------------------------")

    segundaTupla = 3, 6, 9  # definindo uma nova tupla
    print("Segunda Tupla:", segundaTupla)
    print("-----------------------------------")

    print("Tamanho da primeira tupla:", len(primeiraTupla))  # informando o tamanho da tupla
    print("-----------------------------------")

    primeiraTupla += "Novo elemento",
    print("Acrescentando um 'Novo elemento' na tupla:", primeiraTupla)
    print("-----------------------------------")

    print("Tipo de dados:", type(primeiraTupla))
    print("-----------------------------------")

    print("Buscando o 3 na primeira tupla:", primeiraTupla[2])
    print("-----------------------------------")

    primeiraTupla += (4.8, 9)  # concatenação entre tuplas
    print("Foi criada uma tupla '(4.8, 9)' e foi concatenada com a primeira tupla:", primeiraTupla)
    print("-----------------------------------")

    primeiraTupla = primeiraTupla * 6  # multiplicando a quantidade de elementos pelo número informado
    print(primeiraTupla)
    print("-----------------------------------")


tuplaInicio()
