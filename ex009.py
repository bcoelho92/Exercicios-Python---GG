from calendar import c


print("\nTabuada\n")

n = int(input("Digite a tabuada que gostaria de saber: ")) 
#c = 0

print("-"*12)

for c in range (11): 
    print ("{} x {} = {}".format(n,c,n*c))
    #c = +1
    
print("-"*12)

print("\nFim do programa!\n")