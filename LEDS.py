# calculo de leds
EMPRESA = input('Qual empresa você quer contratar, THE VOICE, PUBLIX, MANAUS MIDIAS, PURAKA, VIA DIRETA ou BIG FISH? ')
SABE_NUM_INSER = input('Você sabe o número de inserções por dia? Digite: SIM ou NAO ')

empr = EMPRESA.upper()
num_inser = SABE_NUM_INSER.upper()

if empr == 'THE VOICE':
        VAR_INSER = 2.75
        PLACAS = 10
elif txt == 'PUBLIX':
        VAR_INSER = 2.95
        PLACAS = 5
elif txt == 'MANAUS MIDIAS':
        VAR_INSER = 2.10
        PLACAS = 4
elif txt == 'PURAKA':
        VAR_INSER = 2.75
        PLACAS = 2
elif txt == 'VIA DIRETA':
        VAR_INSER = 3.90
        PLACAS = 2
elif txt == 'BIG FISH':
        VAR_INSER = 2.75
        PLACAS = 1

if num_inser == ('SIM'):
    print('O valor de cada inserção com essa empresa é de R$ ',VAR_INSER,)
    DIAS = int(input('Quantos dias você que exibir? '))
    print('essa empresa possui ', PLACAS, ' placas disponíveis para veiculação')
    QNT_PLACAS = int(input("Quantas placas você quer contratar? "))
    QNT_INSER = int(input('Quantas inserções você vai querer por placa? '))
    print(f'O valor total da veiculação será R$ {DIAS * QNT_PLACAS * QNT_INSER * VAR_INSER}')

if num_inser == ('NAO'):
    ORCAMENTO = int(input('Qual é o seu orçamento para essa campanha? apenas numeros'))
    print('O valor de cada inserção com essa empresa é de R$ ', VAR_INSER, )
    DIAS2 = int(input('Quantos dias você que exibir? '))
    print('essa empresa possui ', PLACAS, ' placas disponíveis para veiculação')
    QNT_PLACAS2 = int(input('Quantas placas você quer contratar? '))
    CALC = int(VAR_INSER * DIAS2 * QNT_PLACAS2)
    while int(CALC*VAR_INSER) < ORCAMENTO:
        CALC += 1
    else:
        QNT_INSER2 = int((CALC/DIAS2)/QNT_PLACAS2)
        print (f'O número de inserções diárias para esse orlçamento é de ',QNT_INSER2)