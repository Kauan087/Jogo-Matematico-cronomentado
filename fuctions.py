# Criar linha
def criar_linha(quantidade):
    print('-'*quantidade)

# Função para criar a tabela
def criar_tabela(tempo_str, acertos_str, pontuação_str):
    linha = [
        '------------------------------------',
        '|   TEMPO   | ACERTOS  | PONTUAÇÃO  |',
        '------------------------------------',
        f'| {tempo_str.center(9)} | {acertos_str.center(8)} | {pontuação_str.center(10)} |',
        '------------------------------------'
    ]
    return linha
