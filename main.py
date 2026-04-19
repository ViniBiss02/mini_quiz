import time

print("Bem vindo ao Quiz")
nome = input('Qual é o seu nome ? \n  Nome: ').capitalize()

start = input(f'Olá {nome}! Vamos começar o jogo?\n  Sim ou Não?: ').lower()

if start != 'sim':
    print('Até mais tarde então!')
    quit()
else:
    print('Otimo, vamos para as perguntas!')

score = 0

while True:
    print("OPÇÕES:\n 1 - Metroid\n 2 - Uncharted\n 3 - Zelda\n 4 - Hollow Knight")
    answer_1 = input("Triforce é um objeto magico de uma série de jogos!"
                     "\nQue jogo é esse ?\nResposta: ").capitalize()
    time.sleep(1)

    if answer_1 == 'Zelda':
        print("Parabéns, você acertou !\n")
        score += 1
        break
    else:
        print("Sinto Muito, você errou ! Tente novamente!\n")

while True:
    print("OPÇÕES:\n 1 - Mario\n 2 - Sonic\n 3 - Crash Bandicoot\n 4 - Spyro")
    answer_2 = input("Qual personagem corre para coletar anéis dourados ?\nResposta: ").capitalize()
    time.sleep(1)

    if answer_2 == 'Sonic':
        print("Parabéns, você acertou !\n")
        score += 1
        break
    else:
        print("Sinto Muito, você errou ! Tente novamente!\n")

while True:
    print("OPÇÕES:\n 1 - God of War\n 2 - Dark Souls\n 3 - Doom\n 4 - Devil May Cry")
    answer_3 = input("Kratos é o personagem principal de qual jogo ?\nResposta: ").capitalize()
    time.sleep(1)

    if answer_3 == 'God of war':
        print("Parabéns, você acertou !\n")
        score += 1
        break
    else:
        print("Sinto Muito, você errou ! Tente novamente!\n")

while True:
    print("OPÇÕES:\n 1 - Halo\n 2 - Call of Duty\n 3 - Battlefield\n 4 - Overwatch")
    answer_4 = input("Master Chief é o protagonista de qual série de jogos ?\nResposta: ").capitalize()
    time.sleep(1)

    if answer_4 == 'Halo':
        print("Parabéns, você acertou !\n")
        score += 1
        break
    else:
        print("Sinto Muito, você errou ! Tente novamente!\n")

print(f"Parabéns {nome}, você completou o Quiz com todas as respostas corretas!\n"
      f"pontuação final: {(score /4) * 100}%")

