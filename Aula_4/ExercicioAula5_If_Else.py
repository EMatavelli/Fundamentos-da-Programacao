# Exercício de Programação Python
# Março de 2026
# Prof. Filipe

print ("##########################################################")

print ("      Programa Calculadora com IF - ELIF - ELSE           ")

print ("##########################################################") 


op = input("Digite a opção desejada: 1-SOMA ou 2-SUBTRAÇÃO  ou3-DIVISÃO ou 4-MULTIPLICAÇÃO 5-RAIZ QUADRADA 6-POTENCIAÇÃO")
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

elif (op==2):
    print ("##########################################################")
    print ("           Agora vamos subtrair b de a                    ")
    print ("##########################################################")
    c=a-b
    print("A resposta é:  ",c)

elif (op==3):

	print ("##########################################################")
	print ("           Agora vamos dividir a por b                    ")
	print ("##########################################################")
	   
	c=a/b
	print("A resposta é:  ",c)

elif (op==4):

	print ("##########################################################")
	print ("           Agora vamos multiplicar a por b                ")
	print ("##########################################################")
	   
	c=a*b
	print("A resposta é:  ",c)

elif (op==5):
    print ("##########################################################")
    print ("           Agora vamos Extrair a Raiz de a                ")
    print ("##########################################################")
    c = ( a ** (1/b) )
    print("A resposta é:  ", c)


elif (op==6):
    print ("##########################################################")
    print ("           Agora vamos elevar a a potência de b           ")
    print ("##########################################################")
    c = a ** b
    print("A resposta é:  ",c)

else:

	print ("##########################################################")
	print ("           Escolha outra opção                            ")
	print ("##########################################################")
	      

input ()
