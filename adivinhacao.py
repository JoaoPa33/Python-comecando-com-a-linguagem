print("*"*40)
print("bem vindo")
print("*"*40)

numero_secreto = 42
total_de_tentativas = 3
#rodada = 1

for rodada in range(1, total_de_tentativas):
# while(rodada <= total_de_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas + 1))
    chute = int(input("Digite um numero entre 0 e 100:"))
    # todo input retorna uma string
    print("Você digitou:", chute)

    if(chute < 1 or chute > 100 ):
        print("o numero que vc digitou um número que não esta entre 0 e 100")
        continue
# o continue faz com que o codigo pare e volte para cima
    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (chute == numero_secreto):
        print("Vc acertou")
        break
# o break faz com que o codigo pare aqui e saia do "for rodada in range(1, total_de_tentativas):"
    else:
        if (chute > numero_secreto):
            print("Você errou: O número é menor do que o digitado")
        elif (chute < numero_secreto):
            print("Você errou: O número é maior do que o digitado")

    # a funçao for ja incremente, nao precisa do "rodada = rodada + 1"
    print("_"*20)
print("fim de jogo")
