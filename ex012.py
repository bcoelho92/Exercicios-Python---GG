print("\nCalculando Descontos\n")

produto = float(input("Digite o vamor do produto. R$ "))

print('''
O produto que custava R$ {},na promoção dom desconto de 5% vai custar R$ {}.

Parabens!'''.format(produto,produto-(produto*5/100)))

print("\nFim do programa!\n")