print("*"*40)
print("bem vindo")
print("*"*40)

numero_secreto = 42
total_de_tentativas = 3
#rodada = 1

for rodada in range(1, total_de_tentativas):
# while(rodada <= total_de_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas + 1))
    chute = int(input("Digite um numero:"))
    # todo input retorna uma string
    print("Você digitou:", chute)

    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (chute == numero_secreto):
        print("Vc acertou")
    else:
        if (chute > numero_secreto):
            print("Você errou: O número é menor do que o digitado")
        elif (chute < numero_secreto):
            print("Você errou: O número é maior do que o digitado")

    # a funçao for ja incremente, nao precisa do "rodada = rodada + 1"
    print("_"*20)
print("fim de jogo")
