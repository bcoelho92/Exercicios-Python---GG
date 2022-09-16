print ("\nPintando Parede.\n")

lr = float(input("Digite a largura da parede: "))
al = float(input("\nDigite a Altura da parede: "))

print('''
\nA área da sua parede é de {}x{} total de {}m².
E para pintar essa area vocêvai precisar de Aproximadamente {} litros de Tinta.
'''.format(lr,al,lr*al,(lr*al)/2))

print("\nFim do programa!\n")