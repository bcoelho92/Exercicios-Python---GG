# Area a de testes 

'''
variável
- valores: int, str, float, bool
- estrutura de dados: list, tuple, dict
- funcoes: def
'''
#### TESTE - DIFERENÇA ENTRE FUNÇÃO E VARIAVEL 
'''
x = 10 # variável com um valor inteiro armazenado
print(type(x))
def x(): # volta para 3 e executa todos os código dentro desse contexto
    return 20
x() # volta para 3 e executa todos os código dentro desse contexto
print(type(x))
x = 15
x()
'''   

# MODULOS
'''
import math

num =  float(input("digite um numero: "))

raiz = math.sqrt(num) #raiz quadrada com modulo 
print('A raiz do numero {} é {:.2f}'.format(num,raiz))
'''
# Cores no Terminal / ANSI

# BASE PARA CORES É O \033[ estilo ; texto; background m EX:\033[1;33;44m....\033
'''
import math

num =  float(input('\033[1;33;44mDigite um numero:\033[m ')) # TESTO FORMATADO COM CORES

raiz = math.sqrt(num)

print('\033[2;35;41mA raiz do numero {} é {:.2f}\033[m \003'.format(num,raiz))
'''
# Estrutura de repetição for
'''
import math

num =  float(input("Digite o numero: "))

for c in range(0,6):
    print("vamo que vamo! {}".format(num))

print("\nFim!")
'''

# Estrutura de repetição while
'''
op = 'S'
while op == 'S':
    n = int(input("Digite um numero: "))
    op = str(input("Deseja continuar [S/N]: ")).upper()
print("Fim! ")
'''
# Interrompendo repetições while - https://www.youtube.com/watch?v=1OFp_-R2B2A

'''
menu = 1
a = float(input("digite um numero: "))
b = float(input("digite outro numero: "))
r = 0

def soma():
    r=a+b
    print(r)
    return r

def dividi():
    r=a%b
    print(r)
    return r
   
menu = print("
    **** BOM DIA ! ***** 

    TESTE DE MENU!

    DIGITE 1 PARA SOMAR
    DIGITE 2 PARA DIVIDIR
    DIGITE 3 SAIR
")

o = int(input("\nDigite opção: "))
while o ==1:
    if o== 1:
        soma()
    elif o==2:
        dividi()
    elif o==3:
        print("SAIR, FIM DO PROGRAMA!")
        break
    else:
        o = int(input("Digite opção correta: "))
'''
#### TESTE LISTA ##### 
'''
nomes_list = ['bruno', 'lucio','carlos']
idade_list = ['14','30','25']
estado_list = ['São Roque', 'Brasilia', 'São Paulo']
print(nomes_list)
print(idade_list)
print(estado_list)
'''
### função, variavel Global e local(dentro da função)
def nome1(nome='fulano GG'):
    print( f'''
    Olá danado(a), seu nome é {nome}, que nome bonito!!

    Fim!\n''')
    return nome
nome = nome1(input("nome: "))
print (f'''
    A seu nome ficou na memoria e é {nome}, só digo uma coisa...
    Programação Orientada a Objeto é o caminho!\n''')

