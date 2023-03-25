print("*"*)
print("bem vindo")
print("*"*40)

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa ", rodada, " de", total_de_tentativas)
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

    rodada = rodada + 1
    print("_"*20)
print("fim de jogo")
