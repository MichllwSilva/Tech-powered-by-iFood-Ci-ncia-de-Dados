# Classe String 

nome = "Michell"
idade = 36
profissao = "programador"   
linguem = "Python"

#fomartos pouco utilizados 
print("Nome: %s idade: %d" % (nome, idade ))   
print("nome: {} idade: {}". format(idade, nome))
print("nome: {1} idade: {0}". format(idade, nome))
print("nome: {nome} idade: {idade}". format(idade = idade, nome = nome))
print("nome: {name} idade: {age} {name} {age} {name}". format(idade, nome))

# F strings maneira mais usada para formatar

print(f" nome: {nome} idade: {idade}")
