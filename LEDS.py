# calculo de leds
EMPRESA = input('Qual empresa você quer contratar, digite o numero: 1. THE VOICE, 2. PUBLIX, 3. MANAUS MIDIAS, 4. PURAKA, 5. VIA DIRETA ou 6. BIG FISH? ')
SABE_NUM_INSER = input('Você sabe o número de inserções por dia? 1. SIM / 2. NAO ')

empr = EMPRESA.upper()
num_inser = SABE_NUM_INSER.upper()

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

if num_inser == ('1'):
    print('O valor de cada inserção com essa empresa é de R$ ',VAR_INSER,)
    DIAS = int(input('Quantos dias você que exibir? '))
    print('essa empresa possui ', PLACAS, ' placas disponíveis para veiculação')
    QNT_PLACAS = int(input("Quantas placas você quer contratar? "))
    QNT_INSER = int(input('Quantas inserções você vai querer por placa? '))
    print(f'O valor total da veiculação será R$ {DIAS * QNT_PLACAS * QNT_INSER * VAR_INSER}')

if num_inser == ('2'):
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