import adivinhacao
import forca
# 1 devemos importar o arquivos
def escolha_jogo():
    print("*"*40)
    print("Escolha um jogo")
    print("*"*40)

    print("Digite o número do jogo que gostaria")
    print("(1) Jogo da forca (2) Jogo da adivinhacao")
    jogo = int(input("Digite o número do jogo:"))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()

    elif (jogo ==2):
        print("Jogando adivinhacao")
        adivinhacao.jogar()
        # 2 colocamos o nome da importacao (da mesma forma que fazemos como uma biblioteca), seguida da def que foi definida no arquivo que será importado
        #   importate aqui ao final da funcao não colocamos ponto

if (__name__ == "__main__"):
    escolha_jogo()  
