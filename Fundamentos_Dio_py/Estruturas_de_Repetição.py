#Comando "for"

Texto = input ("informe um texto")
VOGAIS = "AEIOU"

for letra in Texto:
    if letra.upper() in VOGAIS:
        print(letra,end="") 

else:
  print() #Adiciona uma quebra de linha.   
  print ("Executar no final do laço")

#Range 
  
for numero in range(0, 51, 5):
   print(numero, end="")  
  
