#Venda de Produtos simples usando o else e if
#Menu Inicial
print('Escolha qual produto deseja comprar:')
print('1 - Doritos')
print('2 - Batata Ruffles')
print('3 - Cebolitos')
produto = int(input('Qual é a sua escolha?'))
qtd = int(input('Quantas unidades?'))
#Condicionais
if (produto == 1):
    pagar = qtd * 5.90
    print('Você comprou {} Doritos, valor total a pagar: R${}' .format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 4.40
        print('Você comprou {} Batata Ruffles, valor total a pagar: R${}' .format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 4.29
            print('Você comprou {} Cebolitos, valor total a pagar: R${}' .format(qtd, pagar))
        else:
            (print('Produto Inexistente. :('))
