'''
x = 1
lista = []
print('Digite 4 números.')
while x <= 4:
    n = int(input('Digite um número: '))
    lista.append(n)
    x += 1
media = sum(lista)/len(lista)
print('A media foi:',media)
'''

n1=float(input('digite o primeiro numero: '))
n2=float(input('digite o segundo numero: '))
n3=float(input('digite o terceiro numero: '))
n4=float(input('digite o quarto numero: '))

media = (n1+n2+n3+n4)/4
print('a media é:',media)
