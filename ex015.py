print("\n Aluguel de Carros\n")

dias = int(input("Por qunatos dias você ficou com o veiculo? "))
km = float(input("\nQuantod Km rodados? "))

print(''' 
O aluguel de para ficar com o carro por {} dias com custo de R$ 60.00 a diaria,
e com {} Km rodaos com custo de R$ 0.60 o Km.

O valor do aluguel fica em R$ {}.

Obrigado!
'''.format(dias*60, km*0.15,(dias*60)+(km*0.15)))