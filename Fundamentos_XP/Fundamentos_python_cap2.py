# Aula 1 A sintaxe da Linguagem. 

#Define o valor do limiar

limiar = 5

menores =[] #criar lista menores 
maiores = [] #criar lista maiores

#divide os números de 1 a 10 em maiores e menores 
for i in range (10):
    if(i < limiar):
       menores.append(i)
    elif (i > limiar):
     maiores.append(i)

#imprime na tela os valores das listas
     print('resultado final')   
     print('menores:', menores)
     print('maiores', maiores)
