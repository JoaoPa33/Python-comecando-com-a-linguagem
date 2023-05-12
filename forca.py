import random


def jogar():
    titulo()
    arquivo = "palavra.txt"
    if arquivo_existe("palavra.txt"):
        criar_arquivo(arquivo)
    arquivo = open("palavra.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
    
    palavra_chave = random.choice(palavra).upper()
    #numero = random.randrange(0, len(palavra))
    #palavra_chave = palavra[numero].upper()
    letras_acertadas = []
    letras_acertadas = ["_" for letra in palavra_chave]
    # for letra in palavra_chave:
    #     letras_acertadas.append("_")
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erro = 0

    while(not acertou and not enforcou):
        chute = pede_chute()
        if chute in palavra_chave:
            letras_acertadas = marca_chute_correto(chute , palavra_chave, letras_acertadas)
        else:
            erro +=1
        desenha_forca(erro)
        
        # print(letras_acertadas)
        # if erro == 6:
        #     print("Vc perdeu")
        #     enforcou = True
        # if "_" not in letras_acertadas:
        #     print("Vc acertou")
        enforcou = erro == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if enforcou:
        print("\033[1;31mVocê perdeu\033[m")
    if acertou:
        print("\033[1;32mVocê ganhou\033[m")
    print(f"A palavra correta era: {palavra_chave}")
    print("Fim de jogo")


def arquivo_existe(doc):
    try:
        a = open(doc, "r")
        a.close()
    except:
        return True
    else:
        return False
        

def criar_arquivo(doc):
    a = open(doc, "wt+") 
    a.close()   


def titulo():
    print("*"*40)
    print("BEM VINDO")
    print("*"*40)


def pede_chute():
    return input("Qual a sua letra? ").strip().upper()


def marca_chute_correto(chute, palavra_chave, letras_acertadas):
    for index, letra in enumerate(palavra_chave):
                if chute == letra:
                    letras_acertadas[index] = letra
    return letras_acertadas


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if (__name__ == "__main__"):
    jogar()    
