
tiempo = int(input('Ingresa el periodo deseado en segundos: '))

minu = tiempo / 60
segtol= 60*(minu-int(minu))
hs = minu / 60
mintotal= 60*(hs-int(hs))
dias = hs / 24
hstotal= 24*(dias-int(dias))

print('Los ', tiempo, 'segundos equivalen a ',int(dias), 'dias',int(hstotal), 'horas', int(mintotal), 'minutos y ',int(segtol), 'segundos')

