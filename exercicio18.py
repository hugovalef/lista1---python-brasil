n = float(input('digite o tamanho do arquivo em MB: '))
l = float(input('digite a velocidade do seu link de internet em Mbps: '))

t = (n*8)/l

print('o tempo de download do arquivo sera: %d segundos'%t)


