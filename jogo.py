import random

def escolher_dificuldade():
    print("Escolha um nível de dificuldade:")
    print("1. Fácil (8 tentativas)")
    print("2. Médio (5 tentativas)")
    print("3. Difícil (3 tentativas)")
    
    while True:
        escolha = input("Digite o número do nível de dificuldade: ")
        if escolha == '1':
            return 8
        elif escolha == '2':
            return 5
        elif escolha == '3':
            return 3
        else:
            print("Escolha inválida. Tente novamente.")

numero_secreto = random.randint(1, 10)

max_tentativas = escolher_dificuldade()

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

for tentativas in range(1, max_tentativas + 1):
    tentativas_restantes = max_tentativas - tentativas + 1
    palpite = int(input(f"Digite seu palpite (Tentativa {tentativas}, Tentativas restantes: {tentativas_restantes}): "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).")
        break
    elif palpite < numero_secreto:
        print("O numero e menor, Tente novamente.")
    else:
        print("O numero e maior, Tente novamente.")

if palpite != numero_secreto:
    print(f"Fim do jogo! O número era {numero_secreto}.")