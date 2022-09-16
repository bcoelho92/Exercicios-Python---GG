print("\nConversor de Medidas\n")

m = float(input("digite a distancia em metros: "))
c = m*100
ml = m*1000

print ('''
A distancia digitada foi de {} metros

Qua convertida em centimetros é de {:.0f} cm.

E em milimetros é de {:.0f} mn'''.format(m,c,ml))

print ("\nFim do programa!\n")