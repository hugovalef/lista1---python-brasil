n1=int(input('entre com um numero inteiro: '))
n2=int(input('entre com outro numero inteiro: '))
n3=float(input('entre com algum numero real: '))

print('\na. O produto do primeiro com o dobro do segundo vale: {:.2f}\n'
      'b. A soma do triplo do primeiro com o terceiro vale: {:.2f}\n'
      'c. O terceiro elevado ao cubo vale: {:.2f}'
      .format(n1*2*n2,3*n1+n3,n3**3)
      )


