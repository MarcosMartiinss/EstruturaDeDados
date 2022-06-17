print("Definição de Vetores")

def main():
    vetorVazio = []
    vetorVazio2: list

    print("Tamanho do vetor vazio é: ", len(vetorVazio))
    for i in range(9):
        vetorVazio.append(i)

    print("Novo Tamanho do vetor vazio é: ", len(vetorVazio))
    print("Valores agora no vetor vazio são: ", vetorVazio)

    vetorInteiros = [1, 2, 3, 4, 5, 6, 7]

    print("Valores do vetor inteiros são: ", vetorInteiros)

    for i in range(0, len(vetorInteiros)):
        print("O Valor na posição", i, "é: ", vetorInteiros[i])

    vetorCaracteres = ["Maria", "Gui", "Jô", "Edu", "João", "Carlos", "Joaquina"]

    for i in range(len(vetorCaracteres)):
        print("O Valor na posição", i, "é: ", vetorCaracteres[i])

    vetoresReais = [1.2, 3.5, 12.3, 4.2]
    print("Valores no vetorReais são: ", vetoresReais)

main()