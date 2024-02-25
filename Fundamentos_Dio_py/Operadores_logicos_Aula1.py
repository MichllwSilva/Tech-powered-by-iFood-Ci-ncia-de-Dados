#Conhecendo os operadores logicos 
# Utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica e o resultado do retorno é um boleano.

# And = para ser TRUE todos tem que ser TRUE
# OR = paser TRUE apenas um tem que ser TRUE

#exemplo

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
Saque = 200
limite = 100
conta_especial = True

exp = saldo >= Saque and Saque <=limite or conta_especial and saldo >= Saque
print(exp)
