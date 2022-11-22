
#@------------------#
#@ Teste das Saídas #
#@------------------#

def compararSaidas(arquivo1, arquivo2):
    with open (arquivo1, 'r', encoding='utf-8') as ler:
        arq1 = ler.read()
    with open (arquivo2, 'r', encoding='utf-8') as ler:
        arq2 = ler.read()
    for i in range(len(arq1)):
        if arq1[i] != arq2[i]:
            print('erro: ', i)
            print(arq1[i:i + 60])
            break
    stringSaida = ('||' + '  ' + 'Saidas compativeis = ' + str(arq1 == arq2) + '  ' + '||')
    print('\t' + '=' * len(stringSaida))
    print('\t' + stringSaida)
    print('\t' + '=' * len(stringSaida))
