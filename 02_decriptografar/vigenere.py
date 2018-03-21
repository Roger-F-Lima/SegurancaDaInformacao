import time


def cifrar(texto, chave):

    chave_t = ""
    i = 0
    for letra in texto:

        if ord(letra.upper()) >= 65 and ord(letra.upper()) <= 90:
            if i >= len(chave):
                i = 0
                chave_t += chave[i].upper()
                i += 1
            else:
                chave_t += chave[i].upper()
                i += 1
        else:
            chave_t += letra

    texto_cifrado = ""

    for i in range(len(texto)):
        if texto[i] != " ":
            valor = (ord(texto[i].upper()) + ord(chave_t[i].upper()))%26
            texto_cifrado += chr(valor+65)
        else:
            texto_cifrado += texto[i]
    return texto_cifrado


def decifrar(texto_cifrado, chave):

    chave_tamanho = ""
    i = 0
    for letra in texto_cifrado:
        if ord(letra.upper()) >= 65 and ord(letra.upper()) <= 90:
            if i >= len(chave):
                i = 0
                chave_tamanho += chave[i].upper()
                i += 1
            else:
                chave_tamanho += chave[i].upper()
                i += 1
        else:
            chave_tamanho += letra

    texto_decifrado = ""
    for i in range(len(texto_cifrado)):
        if ord(texto_cifrado[i].upper()) >= 65 and ord(texto_cifrado[i].upper()) <= 90:
            valor = (ord(texto_cifrado[i].upper()) - ord(chave_tamanho[i].upper())) % 26
            texto_decifrado += chr(valor+65)
        else:
            texto_decifrado += texto_cifrado[i]
    return texto_decifrado



def brutalforce():

    data_inicial="Iniciou: %s" %time.ctime()
    tempo_execucao=open("tempo_de_execucao.txt","w")
    possiveis=open("possiveis_chaves_satisfatoria.txt","w")
    cifrado=open("texto_cifrado_amor.txt","r")
    texto = cifrado.read()
    tempo_execucao.write(data_inicial)
    alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        for l1 in alfabeto:
            for l2 in alfabeto:
                for l3 in alfabeto:
                    for l4 in alfabeto:
                        for l5 in alfabeto:
                            for l6 in alfabeto:
                                for l7 in alfabeto:
                                    for l8 in alfabeto:
                                        ultima_chave = open("ultima_chave.txt", "w")
                                        chave="%s%s%s%s%s%s%s%s" %(l1,l2,l3,l4,l5,l6,l7,l8)
                                        ultima_chave.write(chave)
                                        ultima_chave.close()

                                        decifrado=decifrar(texto,chave)
                                        if decifrado.find("AMOR") > 0:
                                            possiveis.writelines("CHAVE: %s\nTEXTO:%s\nDATA:%s\n=====================\n"%(chave,decifrado,time.ctime()))

        data_final = "Finalizou: ", time.ctime()
        tempo_execucao.writelines(data_final)
        tempo_execucao.close()
    except KeyboardInterrupt:
        possiveis.close()
        tempo_execucao.close()
        cifrado.close()

brutalforce()























