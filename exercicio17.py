import math
area = float(input('Digite o tamanho da area a ser pintada em metros quadrados: '))
litros = (area/6)*1.1

latas = (litros/18)
latas = math.ceil(latas)

galoes = (litros/3.6)
galoes = math.ceil(galoes)

#misturando latas e galoes
mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1


print('- Comprando apenas latas\nA quantidade de latas será: %d \nPreço total: R$%.2f\n'%(latas, latas*80))
print('- Comprando apenas galões\nA quantidade de galÕes será: %d \nPreço total: R$%.2f\n '%(galoes, galoes*25))
print('Misturando latas e galões teremos: \n %d latas \n %d galão(ões) \npreco total: R$%.2f'
      %(mixLatas, mixGaloes, mixLatas*80+mixGaloes*25))
