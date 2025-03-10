print("SEJA MUITO BEM VINDO AO JOGO DE ADIVINHAÇÃO")
numerosecreto = 89
palpite = int(input("Digite seu número de palpite:"))

if palpite < numerosecreto:
    print( "O número secreto é maior")

elif palpite > numerosecreto:
    print("O Número secreto é menor.")

else:
    print("Você acertou o número!")