h=float(input('digite a altura da pessoa em metros: '))
pesoidealhomem = 72.7*h-58
pesoidealmulher = 61.1*h-44.7
genero = input('digite o genero (h/m): ')
while genero != 'h' and genero != 'm':
    genero = input('digite "h" ou "m": ')

if genero == 'h':
    print('o peso ideal dessa pessoa é: ',pesoidealhomem, 'kg')
else:
    print('o peso ideal dessa pessoa é: ', pesoidealmulher, 'kg')
