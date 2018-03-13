def montar_matriz(chave):

    """ Monta uma matriz 5x5 com a chave fornecida pelo usuario """

    matriz_aux = []
    # Percorre a chave e verifica se a letra estar no vetor "matriz_aux", caso não esteja
    # a letra é adicionada no mesmo
    for letra in chave.upper():
        if letra not in matriz_aux:
            matriz_aux.append(letra)

    alfabeto = "ABCDEFGHIJLMNOPQRSTUVWXYZ"

    # Adiciona as letras restantes ao vetor
    for letra in alfabeto:
        if letra not in matriz_aux:
            matriz_aux.append(letra)

    matriz_final = []

    p = 0
    q = 5
    for i in range(5):
        matriz_final.append(matriz_aux[p:q])
        p = q
        q += 5
    return matriz_final


def imprimi_matriz_5x5(matriz):

    print("", matriz[0], "\n", matriz[1], "\n", matriz[2], "\n", matriz[3], "\n", matriz[4])


def monta_pares(mensagem):
    """Esta função recebe uma mensagem e transforma em pares"""

    # Pega mensagem original, retira os espaços
    mensagem_final = []
    for letra in mensagem:
        if letra != " ":
            mensagem_final.append(letra.upper())

    # Percorre o vetor que contem a mensagem e Verifica se existe pares com letras
    # iguais, caso haja é adicionado X ou Z
    i = 0
    for e in range(len(mensagem_final) // 2):
        if mensagem_final[i] == mensagem_final[i + 1] and mensagem_final[i] != "X":
            mensagem_final.insert(i + 1, 'X')
        elif mensagem_final[i] == mensagem_final[i + 1] and mensagem_final[i] == "X":
            mensagem_final.insert(i + 1, 'Z')
        i = i + 2

    # Verifica se tem uma letra sobrando nos pares e caso haja é adicionado
    # X ou Z
    if len(mensagem_final) % 2 == 1:
        if mensagem_final[len(mensagem_final) - 1] == "X":
            mensagem_final.append("Z")
        else:
            mensagem_final.append("X")

    i = 0
    em_grupos = []
    for x in range(1, len(mensagem_final) // 2+1):
        em_grupos.append(mensagem_final[i:i+2])
        i = i+2

    return em_grupos


def pega_posicao(matriz_chave, letra):
    """Esta função retorna a posição da letra na Matriz 5x5"""
    x = 0
    y = 0
    for j in range(5):
        for l in range(5):
            if matriz_chave[j][l] == letra:
                x = j
                y = l
    return x, y


def cifrar(chave, mensagem):
    """Esta Função Cifra a mensagem com a chave e retorna cifrada"""

    mensagem_grup = monta_pares(mensagem)
    matriz_chave = montar_matriz(chave)
    cifra = []

    for letra in mensagem_grup:
        l1, c1 = pega_posicao(matriz_chave, letra[0])
        l2, c2 = pega_posicao(matriz_chave, letra[1])
        if l1 == l2:

            if c1 < 4 and c2 < 4:
                c1 += 1
                c2 += 1
            elif c1 < 4 and c2 == 4:
                c1 += 1
                c2 = 0
            elif c1 == 4 and c2 < 4:
                c1 = 0
                c2 += 1

            cifra.append(matriz_chave[l1][c1])
            cifra.append(matriz_chave[l1][c2])

        elif c1 == c2:
            if l1 < 4 and l2 < 4:
                l1 += 1
                l2 += 1
            elif l1 < 4 and l2 == 4:
                l1 += 1
                l2 = 0
            elif l1 == 4 and l2 < 4:
                l1 = 0
                l2 += 1
            cifra.append(matriz_chave[l1][c1])
            cifra.append(matriz_chave[l2][c2])
        else:
            cifra.append(matriz_chave[l1][c2])
            cifra.append(matriz_chave[l2][c1])

    cifra_final = ""

    for letra in cifra:
        cifra_final += letra

    return cifra_final


def pares_cifrados(cifra):
    """Esta função retorna uma matriz 2x13"""
    i = 0
    pares = []
    for x in range(len(cifra) // 2):
        pares.append(cifra[i:i+2])
        i = i+2
    return pares


def decifrar(chave, cifra):
    """Esta funçao decifra a mensagem (Cifrada) com a chave fornecida corretamente"""
    cifra_v = []

    for letra in cifra:
        cifra_v.append(letra)

    cifra_grup = pares_cifrados(cifra_v)
    matriz_chave_c = montar_matriz(chave)
    decifrado = []

    for letra in cifra_grup:
        l1, c1 = pega_posicao(matriz_chave_c, letra[0])
        l2, c2 = pega_posicao(matriz_chave_c, letra[1])
        if l1 == l2:

            if c1 > 0 and c2 > 0:
                c1 -= 1
                c2 -= 1
            elif c1 > 0 and c2 == 0:
                c1 -= 1
                c2 = 4
            elif c1 == 0 and c2 > 0:
                c1 = 4
                c2 -= 1

            decifrado.append(matriz_chave_c[l1][c1])
            decifrado.append(matriz_chave_c[l1][c2])

        elif c1 == c2:
            if l1 > 0 and l2 > 0:
                l1 -= 1
                l2 -= 1
            elif l1 > 0 and l2 == 0:
                l1 -= 1
                l2 = 4
            elif l1 == 0 and l2 > 0:
                l1 = 4
                l2 -= 1
            decifrado.append(matriz_chave_c[l1][c1])
            decifrado.append(matriz_chave_c[l2][c2])
        else:
            decifrado.append(matriz_chave_c[l1][c2])
            decifrado.append(matriz_chave_c[l2][c1])

        for i in range(len(decifrado)):
            try:
                if "X" in decifrado or "Z" in decifrado:
                    decifrado.remove("X")
                    decifrado.remove("Z")
            except ValueError:
                pass

    mensagem_decifrada = ""

    for letra in decifrado:
        mensagem_decifrada += letra

    return mensagem_decifrada


k = str(input("Digite a chave: "))
m = str(input("Digite a mensagem: "))
escolha = int(input("1 - Cifrar, 2 - Decifrar:\n Escolha: "))
if escolha == 1:
    print("")
    print ("\t\tMatriz 5x5")
    imprimi_matriz_5x5(montar_matriz(k))
    print("\n MENSAGEM CIFRADA\n")
    print(cifrar(k, m))
elif escolha == 2:
    print("MENSAGEM CIFRADA: ", m)
    print("\nMENSAGEM DECIFRADA\n")
    print(decifrar(k, m))
