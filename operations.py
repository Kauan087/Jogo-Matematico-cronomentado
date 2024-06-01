from random import *
import time
from fuctions import *

# adição
def addition(dificuldade):
    global fim_tempo, tabelas, linha
    cont = 0
    acertos = 0
    inicio_tempo = time.time()
    # sistema de dificuldade
    if dificuldade:
        n1 = 0
        n2 = 0
        if dificuldade == 1:
            n1 += 0
            n2 += 10
        elif dificuldade == 2:
            n1 += 0
            n2 += 1000
        else:
            n1 += 873
            n2 += 18293

        while cont < 10:
            numero_01 = randint(n1, n2)
            numero_02 = randint(n1, n2)
            resultado_facil = numero_01 + numero_02
            # Pergunta
            while True:
                try:
                    pergunta = int(input(f'Quanto é {numero_01} + {numero_02}? '))
                    break
                except ValueError or TypeError:
                    print('digite um numéro inteiro!')

            cont += 1
            # conferir o resultado
            if pergunta == resultado_facil:
                acertos += 1

            # quer continuar?
            if cont == 10:
                fim_tempo = time.time()
                duração = fim_tempo - inicio_tempo
                minutos, segundos = divmod(int(duração), 60)

                # sistema de pontuação
                erros = 0
                erros += 10 - acertos
                pontuação = 0
                if duração <= 15 and erros == 0:
                    pontuação += 1000
                else:
                    pontuação = duração * 100

                pontuação_final = 1000 - pontuação

                if erros == 0 and duração >= 16:
                    penalidade = pontuação_final - segundos * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final


                elif erros >= 1 and duração >= 5:
                    penalidade = pontuação_final - erros * 115 - segundos * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 5:
                    penalidade = pontuação_final - erros * 85 - duração * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 8:
                    penalidade = pontuação_final - erros * 70 - duração * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                if erros == 9:
                    pontuação_final = 21

                if erros == 10:
                    pontuação_final = 0

                if pontuação_final <= 0:
                    pontuação_final = 0
                # tabela
                tempo_str = f'{minutos}m:{segundos}s'
                acertos_str = f'{10 - erros}'
                pontuação_str = f'{pontuação_final}'
                linha = [
                    '------------------------------------',
                    '|   TEMPO   | ACERTOS  | PONTUAÇÃO  |',
                    '------------------------------------',
                    f'| {tempo_str.center(9)} | {acertos_str.center(8)} | {pontuação_str.center(10)} |',
                    '------------------------------------'
                ]

                # Criar arquivo txt
                with open('arquivo.txt', 'w') as arquivo:
                    for linhas in linha:
                        arquivo.write(linhas + '\n')
                # imprimir arquivo txt
                with open('arquivo.txt') as arquivo:
                    for linha in arquivo:
                        print(linha.rstrip())

                print('[ 1 ] SIM')
                print('[ 2 ] NÃO')
                criar_linha(30)
                # pergunta se o usuário quer continuar o jogo
                while True:
                    try:
                        choice_continue = int(input('deseja continuar?: '))
                        if choice_continue <= 0 or choice_continue >= 3:
                            print('opção ínvalida! ')
                        if choice_continue == 1:
                            cont = 0
                            minutos = 0
                            segundos = 0
                            acertos = 0
                            pontuação_final = 0
                            inicio_tempo = time.time()
                            break
                        elif choice_continue == 2:
                            break
                    except ValueError or TypeError:
                        print('opção ínvalida! ')
                    criar_linha(30)


def Subtraction(dificuldade: object) -> object:
    
    global fim_tempo, tabelas, linha
    cont = 0
    acertos = 0
    inicio_tempo = time.time()
    # sistema de dificuldade
    if dificuldade:
        n1 = 0
        n2 = 0
        if dificuldade == 1:
            n1 += 0
            n2 += 20
        elif dificuldade == 2:
            n1 += 0
            n2 += 1000
        else:
            n1 += 829
            n2 += 18283

        while cont < 10:
            numero_01 = randint(n1, n2)
            numero_02 = randint(n1, n2)
            if numero_01 < numero_02:
                numero_01, numero_02 = numero_02, numero_01

            # conferir o resultado
            resultado_facil = numero_01 - numero_02

            # Pergunta
            while True:
                try:
                    pergunta = int(input(f'Quanto é {numero_01} - {numero_02}? '))
                    break
                except ValueError or TypeError:
                    print('digite um numéro inteiro!')

            cont += 1
            if pergunta == resultado_facil:
                acertos += 1

            # quer continuar?
            if cont == 10:
                fim_tempo = time.time()
                duração = fim_tempo - inicio_tempo
                minutos, segundos = divmod(int(duração), 60)

                # sistema de pontuação
                erros = 0
                erros += 10 - acertos
                pontuação = 0
                pontuação_final = 0
                if duração <= 15 and erros == 0:
                    pontuação_final += 1000
                else:
                    pontuação = duração * 100

                pontuação_final = 1000 - pontuação

                if erros == 0 and duração <= 60:
                    penalidade = pontuação_final - segundos * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final


                elif erros >= 1 and duração >= 5:
                    penalidade = pontuação_final - erros * 115 - segundos * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 5:
                    penalidade = pontuação_final - erros * 85 - duração * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 8:
                    penalidade = pontuação_final - erros * 70 - duração * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                if erros == 9:
                    pontuação_final = 21

                if erros == 10:
                    pontuação_final = 0

                if pontuação_final <= 0:
                    pontuação_final = 0
                # tabela
                tempo_str = f'{minutos}m:{segundos}m'
                acertos_str = f'{10 - erros}'
                pontuação_str = f'{pontuação_final}'
                linha = [
                    '------------------------------------',
                    '|   TEMPO   | ACERTOS  | PONTUAÇÃO  |',
                    '------------------------------------',
                    f'| {tempo_str.center(9)} | {acertos_str.center(8)} | {pontuação_str.center(10)} |',
                    '------------------------------------'
                ]

                with open('arquivo.txt', 'w') as arquivo:
                    for linhas in linha:
                        arquivo.write(linhas + '\n')

                with open('arquivo.txt') as arquivo:
                    for linha in arquivo:
                        print(linha.rstrip())

                print('[ 1 ] SIM')
                print('[ 2 ] NÃO')
                criar_linha(30)
                while True:
                    try:
                        choice_continue = int(input('deseja continuar?: '))
                        if choice_continue <= 0 or choice_continue >= 3:
                            print('opção ínvalida! ')
                        if choice_continue == 1:
                            cont = 0
                            minutos = 0
                            segundos = 0
                            acertos = 0
                            pontuação_final = 0
                            inicio_tempo = time.time()
                            break
                        elif choice_continue == 2:
                            break
                    except ValueError or TypeError:
                        print('opção ínvalida! ')
                    criar_linha(30)


def Multiplication(dificuldade):
    global fim_tempo, tabelas, linha, numero_02
    cont = 0
    acertos = 0
    inicio_tempo = time.time()
    # sistema de dificuldade
    if dificuldade:
        n1 = 0
        n2 = 0
        if dificuldade == 1:
            n1 += 0
            n2 += 10
        elif dificuldade == 2:
            n1 += 15
            n2 += 100

        else:
            n1 += 20
            n2 += 1829

        while cont < 10:
            numero_01 = randint(n1, n2)
            numero_02 = randint(n1, n2)
            if dificuldade == 2:
                numero_02 = randint(1, 20)
            elif dificuldade == 3:
                numero_02 = randint(20, 100)
            # conferir o resultado
            resultado_facil = numero_01 * numero_02

            # Pergunta
            while True:
                try:
                    pergunta = int(input(f'Quanto é {numero_01} x {numero_02}? '))
                    break
                except ValueError or TypeError:
                    print('digite um numéro inteiro!')

            cont += 1
            if pergunta == resultado_facil:
                acertos += 1

            # quer continuar?
            if cont == 10:
                fim_tempo = time.time()
                duração = fim_tempo - inicio_tempo
                minutos, segundos = divmod(int(duração), 60)

                # sistema de pontuação
                erros = 0
                erros += 10 - acertos
                pontuação = 0
                pontuação_final = 0
                if duração <= 15 and erros == 0:
                    pontuação_final += 1000

                else:
                    pontuação = duração * 100
                pontuação_final = 1000 - pontuação

                if erros == 0 and duração >= 15:
                    penalidade = pontuação_final - segundos * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final


                elif erros >= 1 and duração >= 5:
                    penalidade = pontuação_final - erros * 115 - segundos * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 5:
                    penalidade = pontuação_final - erros * 85 - duração * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 8:
                    penalidade = pontuação_final - erros * 70 - duração * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                if erros == 9:
                    pontuação_final = 21

                if erros == 10:
                    pontuação_final = 0

                if pontuação_final <= 0:
                    pontuação_final = 0
                # tabela
                tempo_str = f'{minutos}m:{segundos}s'
                acertos_str = f'{acertos}'
                pontuação_str = f'{pontuação_final}'
                linha = [
                    '------------------------------------',
                    '|   TEMPO   | ACERTOS  | PONTUAÇÃO  |',
                    '------------------------------------',
                    f'| {tempo_str.center(9)} | {acertos_str.center(8)} | {pontuação_str.center(10)} |',
                    '------------------------------------'
                ]

                with open('arquivo.txt', 'w') as arquivo:
                    for linhas in linha:
                        arquivo.write(linhas + '\n')

                with open('arquivo.txt') as arquivo:
                    for linha in arquivo:
                        print(linha.rstrip())

                print('[ 1 ] SIM')
                print('[ 2 ] NÃO')
                criar_linha(30)
                while True:
                    try:
                        choice_continue = int(input('deseja continuar?: '))
                        if choice_continue <= 0 or choice_continue >= 3:
                            print('opção ínvalida! ')
                        if choice_continue == 1:
                            minutos = 0
                            segundos = 0
                            acertos = 0
                            pontuação_final = 0
                            inicio_tempo = time.time()
                            cont = 0
                            break
                        elif choice_continue == 2:
                            break
                    except ValueError or TypeError:
                        print('opção ínvalida! ')
                    criar_linha(30)


def Division(dificuldade):
    global fim_tempo, tabelas, linha
    cont = 0
    acertos = 0
    inicio_tempo = time.time()
    # sistema de dificuldade
    if dificuldade:
        n1 = 0
        n2 = 0
        if dificuldade == 1:
            n1 = 0
            n2 = 10
        elif dificuldade == 2:
            n1 = 15
            n2 = 100
        else:
            n1 = 20
            n2 = 1829

        while cont < 10:
            numero_01 = randint(n1, n2)
            numero_02 = randint(n1, min(numero_01, n2 // 2))

            if numero_02 == 0:
                numero_02 = 1

            numero_01 = numero_02 * randint(1, 10)
            # conferir o resultado
            resultado_facil = numero_01 // numero_02

            # Pergunta
            while True:
                try:
                    pergunta = int(input(f'Quanto é {numero_01} % {numero_02}? '))
                    break
                except (ValueError, TypeError):
                    print('Digite um número inteiro!')

            cont += 1
            # conferir o resultado
            if pergunta == resultado_facil:
                acertos += 1

            # quer continuar?
            if cont == 10:
                fim_tempo = time.time()
                duração = fim_tempo - inicio_tempo
                minutos, segundos = divmod(int(duração), 60)

                # sistema de pontuação
                erros = 0
                erros += 10 - acertos
                pontuação = 0
                pontuação_final = 0
                if duração <= 15 and erros == 0:
                    pontuação_final += 1000
                else:
                    pontuação = duração * 100

                pontuação_final = 1000 - pontuação

                if erros == 0 and duração >= 16:
                    penalidade = pontuação_final - segundos * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final


                elif erros >= 1 and duração >= 5:
                    penalidade = pontuação_final - erros * 115 - segundos * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 5:
                    penalidade = pontuação_final - erros * 85 - duração * 1.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                elif erros >= 8:
                    penalidade = pontuação_final - erros * 70 - duração * 3.5
                    pontuação_final -= penalidade
                    pontuação_final = 1000 - pontuação_final

                if erros == 9:
                    pontuação_final = 21

                if erros == 10:
                    pontuação_final = 0

                if pontuação_final <= 0:
                    pontuação_final = 0
                # tabela
                tempo_str = f'{minutos}m:{segundos}s'
                acertos_str = f'{10 - erros}'
                pontuação_str = f'{pontuação_final}'
                linha = [
                    '------------------------------------',
                    '|   TEMPO   | ACERTOS  | PONTUAÇÃO  |',
                    '------------------------------------',
                    f'| {tempo_str.center(9)} | {acertos_str.center(8)} | {pontuação_str.center(10)} |',
                    '------------------------------------'
                ]

                with open('arquivo.txt', 'w') as arquivo:
                    for linhas in linha:
                        arquivo.write(linhas + '\n')

                with open('arquivo.txt') as arquivo:
                    for linha in arquivo:
                        print(linha.rstrip())

                print('[ 1 ] SIM')
                print('[ 2 ] NÃO')
                criar_linha(30)
                while True:
                    try:
                        choice_continue = int(input('deseja continuar?: '))
                        if choice_continue <= 0 or choice_continue >= 3:
                            print('opção ínvalida! ')
                        if choice_continue == 1:
                            minutos = 0
                            segundos = 0
                            acertos = 0
                            pontuação_final = 0
                            inicio_tempo = time.time()
                            cont = 0
                            break
                        elif choice_continue == 2:
                            break
                    except ValueError or TypeError:
                        print('opção ínvalida! ')
                    criar_linha(30)

