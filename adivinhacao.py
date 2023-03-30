import random

print("*"*40)
print("bem vindo")
print("*"*40)

numero_secreto = random.randrange(0, 101)
total_de_tentativas = 0
pontos = 100
#rodada = 1

print("Qual nível vc gostaria de selecionar?")
nivel = int(input("(1) facil, (2) médio, (3)dificil:"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
# while(rodada <= total_de_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute = int(input("Digite um numero entre 1 e 100:"))
    # todo input retorna uma string
    print("Você digitou:", chute)

    if(chute < 1 or chute > 100 ):
        print("o numero que vc digitou um número que não esta entre 1 e 100")
        continue
# o continue faz com que o codigo pare e volte para cima
    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (chute == numero_secreto):
        print("Vc acertou")
        print("Você fez {} pontos".format(pontos))
        break
# o break faz com que o codigo pare aqui e saia do "for rodada in range(1, total_de_tentativas):"
    else:
        if (chute > numero_secreto):
            print("Você errou: O número é menor do que o digitado")
        elif (chute < numero_secreto):
            print("Você errou: O número é maior do que o digitado")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    # a funçao for ja incremente, nao precisa do "rodada = rodada + 1"
    print("_"*20)
print("fim de jogo")

