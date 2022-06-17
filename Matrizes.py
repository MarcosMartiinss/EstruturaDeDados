def bidimensional():
    bidimensional = [[1, 2, 3, 4], [9, 8, 7, 6]]

    # neste for é acessado o primeiro nível da matriz
    for i in range(0, len(bidimensional)):
        # neste for é acessado o segundo nível, onde contém os dados
        for j in range(0, len(bidimensional[i])):
            print("Bidimensional Valor [", i, ",", j, "]", bidimensional[i][j])


def tridimensional():
    tridimensional = [[[1, 2, 3, 4], [4, 3, 2, 1]], [[9, 8, 7, 5], [4, 5, 6, 7]]]

    # neste for é acessado o primeiro nível da matriz
    for i in range(0, len(tridimensional)):
        # neste for é acessado o segundo nível da matriz
        for j in range(0, len(tridimensional[i])):
            # neste for é acessado o segundo nível da matrzi
            for k in range(0, len(tridimensional[j])):
                print("Tridimensional Valor [", i, ",", j, ",", k, "]: ", tridimensional[i][j][k])


def executarAplicacao():
    print("Exemplo de Matriz (vetor bidimensional)")
    bidimensional()
    print("------------------------")

    print("Exemplo de Matriz de Três dimensões (vetor tridimensional)")
    tridimensional()
    print("------------------------")


executarAplicacao()
