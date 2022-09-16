print("\nDobro, Triplo, Raiz Quadrada\n")

n = int(input("Digite um numero: "))
d = n*2
t = n*3
r = n**(1/2) # raiz quadrada sem formatação


'''
print ('\nO Dobro é: ', n*2)
print ('\nO Triplo é: ', n*3)
print('\nA raiz Quadrada é:', n**(1/2))
'''
print('''
O dobro de {} é {} beleza?
A o triplo de {} é {}.

e por fim a raiz quadrada de {} é {}

valeu! Deixa o like! :) 

'''.format(n,d,n,t,n,pow(n,1/2))) # raiz quadrada pow(n,1/2)


print("\nFim do programa!\n")
