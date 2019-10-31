peso=float(input('digite o peso do peixe em kg: '))
if peso > 50:
    excesso = peso - 50
    print('o excesso a ser pago é: R$ %.2f' %(excesso*4))
else:
    print('nao houve excesso de peso')

