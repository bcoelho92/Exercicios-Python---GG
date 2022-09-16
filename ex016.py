from math import trunc

print("\nQuebrando um número! \m")

valor= float(input("Digite o valor Real EX: 1.55, 5.35, 6.97: "))

print('''
O numero {} tem a sua parte inteira {:.0f} .

Foi!'''.format(valor,valor)) # FORMATAÇÃO :.0F
# PEGA O VALOR ANTES DA , ARREDONDANDO PARA MAIS OU MENOS.
 
print('''
O numero {} tem a sua parte inteira {} .

Foi!'''.format(valor,trunc(valor))) # IMPORT MATH E FUNÇÃO TRUNC
# PEGA O VALOR ANTES DA , SEM ARREDONDAR.

print('''
O numero {} tem a sua parte inteira {} .

Foi!'''.format(valor,int(valor))) # FUNÇÃO INT
# PEGA O VALOR ANTES DA , SEM ARREDONDAR.