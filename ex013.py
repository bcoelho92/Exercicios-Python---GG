print("\nReajuste Salarial!\n")

Salario = float(input("Digite seu salario: R$ "))
ajuste = float(input("digite o percentual de ajuste em % ex: 5,10, 15...:"))
print('''
O seu salario é de R$ {}, com o ajuste de {:.0f} % seu salario atual é R$ {}.

Parabens, novo milionario!'''.format(Salario,ajuste,Salario+(Salario*ajuste/100)))

print("\nFim do programa!\n")