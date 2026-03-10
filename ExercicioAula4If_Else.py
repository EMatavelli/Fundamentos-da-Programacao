# Exercício de Programação Python
# Março de 2026
# Prof. Filipe

print ("##########################################################")

print ("      Programa Calculadora com IF - ELIF - ELSE           ")

print ("##########################################################") 



op = input("Digite 1-SOMA OU 2-SUBTRAÇÃO")
op=int(op)



a = input("Digite o 1o. número:   ")
a = int(a)



b = input("Digite o 2o. número:   ")
b = int(b)

if (op==1):
    

	print ("##########################################################")
	print ("           Agora vamos somar a + b                  ")
	print ("##########################################################")
	
    
    
	c=a+b
	print("A resposta é:  ",c)

else:

	print ("##########################################################")
	print ("           Agora vamos subtrair b de a                    ")
	print ("##########################################################")
	
    
    
	c=a-b
	print("A resposta é:  ",c)

input ()
