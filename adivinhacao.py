print("*"*40)
print("bem vindo")
print("*"*40)

numero_secreto = 42

chute = int(input("Digite um numero:"))
# todo input retorna uma string

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

print("fim de jogo")
