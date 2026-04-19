print("Bem vindo ao Quiz")
nome = input('Qual é o seu nome ? \n  Nome: ')

start = input(f'Olá {nome}! Vamos começar o jogo?\n  Sim ou Não?: ').lower()

if start != 'sim' or 'yes':
    print('Até mais tarde então!')
    quit()
else:
    print('Otimo, vamos para as perguntas!')
