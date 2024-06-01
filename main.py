import operations
from fuctions import *
from operations import *

criar_linha(30)
print('       JOGO DE TABUADA  ')
criar_linha(30)
# escolha de operação
print('''[ 1 ] ADIÇÃO
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO ''')
criar_linha(30)
while True:
    try:
        choice_operation = int(input('Escolha uma operação: '))
        if choice_operation > 4 or choice_operation <= 0:
            print('opção ínvalida! ')
        else:
            break
    except ValueError or TypeError:
        print('opção ínvalida! ')

# escolha dificuldade
criar_linha(30)
# Adição
if choice_operation == 1:
    print('''[ 1 ] FÁCIL
[ 2 ] MÉDIO
[ 3 ] DIFÍCIL''')
    criar_linha(30)
    while True:
        # escolha dificuldade
        try:
            choice_difficult = int(input('Escolha uma dificuldade: '))
            if choice_difficult <= 0 or choice_difficult >= 4:
                print('opção ínvalida! ')
            else:
                break
        except ValueError or TypeError:
            print('opção ínvalida! ')
        criar_linha(30)

    operations.addition(choice_difficult)

# Subtração
if choice_operation == 2:
    print('''[ 1 ] FÁCIL
[ 2 ] MÉDIO
[ 3 ] DIFÍCIL''')
    criar_linha(30)
    # escolha dificuldade
    while True:
        try:
            choice_difficult = int(input('Escolha uma dificuldade: '))
            if choice_difficult <= 0 or choice_difficult >= 4:
                print('opção ínvalida! ')
            else:
                break
        except ValueError or TypeError:
            print('opção ínvalida! ')
        criar_linha(30)

    operations.Subtraction(choice_difficult)

# Multiplicação
if choice_operation == 3:
    print('''[ 1 ] FÁCIL
[ 2 ] MÉDIO
[ 3 ] DIFÍCIL''')
    criar_linha(30)
    # escolha dificuldade
    while True:
        try:
            choice_difficult = int(input('Escolha uma dificuldade: '))
            if choice_difficult <= 0 or choice_difficult >= 4:
                print('opção ínvalida! ')
            else:
                break
        except ValueError or TypeError:
            print('opção ínvalida! ')
        criar_linha(30)

    operations.Multiplication(choice_difficult)

# Divisão
if choice_operation == 4:
    print('''[ 1 ] FÁCIL
[ 2 ] MÉDIO
[ 3 ] DIFÍCIL''')
    criar_linha(30)
    # escolha dificuldade
    while True:
        try:
            choice_difficult = int(input('Escolha uma dificuldade: '))
            if choice_difficult <= 0 or choice_difficult >= 4:
                print('opção ínvalida! ')
            else:
                break
        except ValueError or TypeError:
            print('opção ínvalida! ')
        criar_linha(30)

    operations.Division(choice_difficult)