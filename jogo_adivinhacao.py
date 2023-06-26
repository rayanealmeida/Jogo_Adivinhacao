print('*-' * 15)
print('Jogo da Adivinhação')
print('*-' * 15)
print('\nVocê precisa descobrir o número secreto!\nNosso jogo possui 3 níveis:\n[1] - Fácil: 20 tentativas\n[2] - Intermediário: 10 tentativas\n[3] - Difícil: 5 tentativas\n')

nivel = int(input('Em qual nível você deseja jogar?\n'))
opcao_certa = (1, 2, 3)
while nivel not in opcao_certa:
    nivel = int(input('Você digitou uma opção inválida. Tente novamente. Em qual nível você deseja jogar?\n'))

numero_secreto = 6

if nivel == 1:
    tentativas = 20
    rodada = 1
    while rodada <= tentativas:
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Qual é o seu chute?\n'))

        certo = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if certo:
            print('Você acertou! Parabéns!')
            break
        elif maior:
            print('Você chutou um número maior que o número secreto.\n')
        elif menor:
            print('Você chutou um número menor que o número secreto.\n')

        rodada = rodada + 1

elif nivel == 2:
    tentativas = 10
    rodada = 1
    while rodada <= tentativas:
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Qual é o seu chute?\n'))

        certo = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if certo:
            print('Você acertou! Parabéns!')
            break
        elif maior:
            print('Você chutou um número maior que o número secreto.\n')
        elif menor:
            print('Você chutou um número menor que o número secreto.\n')

        rodada = rodada + 1

elif nivel == 3:
    tentativas = 5
    rodada = 1
    while rodada <= tentativas:
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Qual é o seu chute?\n'))

        certo = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if certo:
            print('Você acertou! Parabéns!')
            break
        elif maior:
            print('Você chutou um número maior que o número secreto.\n')
        elif menor:
            print('Você chutou um número menor que o número secreto.\n')

        rodada = rodada + 1

print('~' * 20)
print('Fim de jogo!')
print('~' * 20)
