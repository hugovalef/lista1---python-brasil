import math
n = float(input('Digite o tamanho da area a ser pintada em metros quadrados: '))
n = n/54
n = math.ceil(n)
print('A quantidade de latas será: %d \nPreço total: R$%.2f '%(n, n*80))
