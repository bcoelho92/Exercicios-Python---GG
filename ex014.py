print("\nConversor de Temperaturas\n")

temp = float(input("Digite a temperatuar em *C: "))

print('''
A temperatura em °C é de {:.1f} convertida para °F fica em {:.1f} graus.

Valeu!
 
'''.format(temp,(temp*9/5)+32))