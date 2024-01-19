# calculo de valores de veiculação em paineis de LED
CONSULTA = input('Você deseja consultar um valor, ou já tem um orçamento definido? 1. Consultar um valor / 2. Orçamento definido ')
empr = input('Qual empresa você quer contratar, digite o numero: 1. LEDS MANAUS, 2. LEDS MANAUS, 3. MIDIA LEDS, 4. TOTAL LEDS, 5. LEDS COMUNICACAO ou 6. PUBLICIDADE LEDS? ')

if empr == '1':
        VAR_INSER = 2.75
        PLACAS = 10
elif empr == '2':
        VAR_INSER = 2.95
        PLACAS = 5
elif empr == '3':
        VAR_INSER = 2.10
        PLACAS = 4
elif empr == '4':
        VAR_INSER = 2.75
        PLACAS = 2
elif empr == '5':
        VAR_INSER = 3.90
        PLACAS = 2
elif empr == '6':
        VAR_INSER = 2.75
        PLACAS = 1
else:
    print('Valor inválido')


if CONSULTA == ('1'):
    print(f'O valor de cada inserção com essa empresa é de R$ {VAR_INSER}')
    periodo1 = int(input('Quantos dias você que exibir? '))
    print(f'essa empresa possui {PLACAS} placas disponíveis para veiculação')
    QNT_PLACAS = int(input("Quantas placas você quer contratar? "))
    QNT_INSER = int(input('Quantas inserções você vai querer por placa, todos os dias? '))
    consulta = periodo1 * QNT_PLACAS * QNT_INSER * VAR_INSER
    print(f'O valor total da veiculação será R$ {consulta}')

if CONSULTA == ('2'):
    ORCAMENTO = int(input('Qual é o seu orçamento para essa campanha? apenas numeros '))
    print(f'O valor de cada inserção com essa empresa é de R$ {VAR_INSER}')
    periodo2 = int(input('Quantos dias você que exibir? '))
    print(f'essa empresa possui {PLACAS} placas disponíveis para veiculação')
    QNT_PLACAS2 = int(input('Quantas placas você quer contratar? '))

    # CALC é o valor que uma inserção em todas as placas em todos os dias vai custar
    # o calculo é adicionar uma inserção em cada placa até atingir o valor limite do orçamento
    # após, fazer o caminho reverso para descobrir quantas inserções foram adicionadas
    # E esse será o resultado que fechará o numero de inserções para o mídia.

    CALC = int(VAR_INSER * periodo2 * QNT_PLACAS2)
    while int(CALC*VAR_INSER) < ORCAMENTO:
        CALC += 1
    else:
        QNT_INSER2 = int((CALC/periodo2)/QNT_PLACAS2)
        print (f'O número de inserções diárias para esse orçamento é de',QNT_INSER2,' por placa')
