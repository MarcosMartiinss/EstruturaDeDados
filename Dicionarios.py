import datetime


def dicionario():
    dicionario = {"nome": "Marcos", "idade": 25, "maiorIdade": True, "salario": 4567.22,
                  "filhos": [{"nome": "Gu", "idade": 3}, {"nome": "Jô", "idade": 10}],
                  "numerosPrimos": [1, 2, 3, 5, 7]}
    print("Dicionário: ", dicionario, "\n")
    print("--------------------------------------------")
    print("Exibir a informação da Idade: ", dicionario["idade"], "\n")
    print("--------------------------------------------")
    print("Teste do get", dicionario.get("caso", 0), "\n")
    print("--------------------------------------------")
    print("Retorna uma tupla (chave, valor): ", dicionario.items(), "\n")
    print("--------------------------------------------")
    print("Retorna somente chaves: ", dicionario.keys(), "\n")
    print("--------------------------------------------")
    print("Retorna somente os valroes: ", dicionario.values(), "\n")
    print("--------------------------------------------")

    dicionario.update({"dataNascimento": datetime.datetime(1997, 3, 29)})
    print("Imprimindo os dados do dicionário")
    for chave, valor in dicionario.items():
        if chave == "dataNascimento":
            print("Exibindo os dados da chave", chave, "ocm o valor", valor.strftime("%d/%m/%Y"))
        elif chave == "filhos":
            for i in range(len(valor)):
                for chaveFilhos, valorFilhos in valor[i].items():
                    print("Exibindo os dados da chave dos filhos",
                          chaveFilhos, "com o valor dos filhos",
                          valorFilhos)
        elif chave == "numerosPrimos":
            for i in range(len(valor)):
                print("Valores primos:", valor[i])
        else:
            print("Exibindo os dados chave", chave, "com o valor", valor)


dicionario()
